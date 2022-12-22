import utils
import re

utils.DEBUG = True
# utils.DEBUG = False
utils.printInfo()

file = utils.fileToLString(utils.inputFilePath())

inputMap = file.split("\n\n")[0]
inputPath = file.split("\n\n")[1]

mapValues = {}
for y, row in enumerate(inputMap.split('\n')):
    for x, value in enumerate(row):
        if value == '#' or value == '.':
            mapValues[(x, y)] = value


initialPosition = None
i = 0
while initialPosition is None:
    if (i, 0) in mapValues:
        initialPosition = (i, 0)
    i += 1

pathValues = []
steps = re.split("([LR])", inputPath)

orientationToVector = {
    0: (1, 0),
    1: (0, 1),
    2: (-1, 0),
    3: (0, -1),
}

vectorToOrientation = {
    (1, 0): 0,
    (0, 1): 1,
    (-1, 0): 2,
    (0, -1): 3,
}

opposites = {}
def findOpposite(x, y, u, v):
    if (x, y, u, v) in opposites:
        return opposites[(x, y, u, v)]

    if u == 0 and v == 0:
        raise Exception('0')

    if u != 0 and v != 0:
        raise Exception('1')

    X, Y = x, y
    U, V = -u, -v
    result = (X, Y)
    while True:
        X += U
        Y += V
        if (X, Y) not in mapValues:
            break
        result = (X, Y, u, v)

    opposites[(x, y, u, v)] = result
    return result


def followPath(steps, initialPosition, findOpposite):
    # x, y, orientation R=0 D=1 L=2 U=3
    state = [initialPosition[0], initialPosition[1], 0]
    for step in steps:
        x, y, orientation = state

        if step == 'L' or step == 'R':
            orientation += 1 if step == 'R' else -1
            orientation %= 4
            state = [x, y, orientation]
            continue

        u, v = orientationToVector[orientation]

        for _ in range(int(step)):
            if (x + u, y + v) in mapValues:
                if mapValues[(x + u, y + v)] != '#':
                    x, y = x + u, y + v
            else:
                # wall
                a, b, u, v = findOpposite(x, y, u, v)
                orientation = vectorToOrientation[(u,v)]
                if mapValues[(a, b)] != '#':
                    x, y = a, b

        state = [x, y, orientation]
    return state


col, row, ori = followPath(steps, initialPosition, findOpposite)
col += 1
row += 1
print('PART1')
print(1000 * row + 4 * col + ori)


# PART 2
assert len(inputMap.split('\n')) % 3 == 0
side = len(inputMap.split('\n')) // 3

sections = {}
# gets which section of the cube the coords are at
def section(x, y):
    if (x, y) in sections:
        return sections[(x, y)]

    if y < side:
        result = 1
    elif y < 2* side:
        if x < side:
            result = 2
        elif x < 2* side:
            result = 3
        else:
            result = 4
    else:
        if x < 3* side:
            result = 5
        else:
            result = 6

    assert 0 < result <= 6

    sections[(x, y)] = result
    return result


opposites = {}
def findOpposite(x, y, u, v):
    if (x, y, u, v) in opposites:
        return opposites[(x, y, u, v)]

    result = (x, y, u, v)
    s = section(x, y)
    if s == 1:
        if (u, v) == (-1, 0):
            result = (side + y, side, 0, 1)
        elif (u, v) == (1, 0):
            result = (4* side -1, 3*side -1 -y, -1, 0)
        elif (u, v) == (0, -1):
            result = (side -1 -(2*side - x), side, 0, 1)
        else:
            raise Exception('3')
    if s == 2:
        if (u, v) == (0, 1):
            result = (2*side -1 -x, 3*side -1, 0, -1)
        elif (u, v) == (-1, 0):
            result = (4*side -1 -(y - side), 3*side -1, 0, -1)
        elif (u, v) == (0, -1):
            result = (3*side -1 -x, 0, 0, 1)
        else:
            raise Exception('3')
    if s == 3:
        if (u, v) == (0, 1):
            result = (2*side, 3*side - 1 -(2*side - 1 -x), 1, 0)
        elif (u, v) == (0, -1):
            result = (2*side, 2*side -1 - y, 0, 1)
        else:
            raise Exception('3')
    if s == 4:
        if (u, v) == (1, 0):
            result = (4*side -1 -(2*side -y), 2*side, 0, 1)
        else:
            raise Exception('3')
    if s == 5:
        if (u, v) == (-1, 0):
            result = (2*side -1 -(3*side -y), 2*side -1, 0, -1)
        elif (u, v) == (0, 1):
            result = (side -1 -(3*side -x), 2*side -1, 0, -1)
        else:
            raise Exception('3')
    if s == 6:
        if (u, v) == (1, 0):
            result = (3*side -1, side -1 - (3*side - y), -1, 0)
        elif (u, v) == (0, 1):
            result = (0, side -1 -(4*side - x), 1, 0)
        elif (u, v) == (0, -1):
            result = (3*side -1, 2*side -1 -(2*side - x), -1, 0)
        else:
            raise Exception('3')

    assert (result[0], result[1]) in mapValues
    opposites[(x, y, u, v)] = result
    return result

print('')
col, row, ori = followPath(steps, initialPosition, findOpposite)
col += 1
row += 1
print('PART2')
print(col, row, ori)
print(1000 * row + 4 * col + ori)
