import utils

# utils.DEBUG = True
utils.printInfo()

lines = utils.fileToLines(utils.inputFilePath())

NORTH, EAST, SOUTH, WEST = '^', '>', 'v', '<'

dirToVector = {
    NORTH: (0, -1),
    EAST: (1, 0),
    SOUTH: (0, 1),
    WEST: (-1, 0),
}

def generateMap(file):
    start = None
    goal = None
    walls = set()
    blizzards = set()
    for y, row in enumerate(file):
        for x, value in enumerate(row):
            if y == 0 and value == '.':
                start = (x, y)
            if y == len(file) - 1 and value == '.':
                goal = (x, y)

            if value == '#':
                walls.add((x, y))

            elif value != '.':
                blizzards.add((x, y, value))

    assert start is not None and goal is not None
    return start, goal, walls, blizzards


memoOpposite = {}
def oppositeWall(walls, pos, vect):
    if pos in memoOpposite:
        return memoOpposite[pos]
    x, y = pos
    u, v = vect
    x, y = x - u, y - v
    while (x, y) not in walls:
        x, y = x - u, y - v
    memoOpposite[pos] = (x, y)
    return memoOpposite[pos]



def nextBlizzardState(walls, blizzards):
    newBlizzard = set()
    for x, y, direction in blizzards:
        xx, yy = x, y
        u, v = dirToVector[direction]
        xx += u
        yy += v

        if (xx, yy) in walls:
            xx, yy = oppositeWall(walls, (xx, yy), (u, v))
            xx += u
            yy += v
        newBlizzard.add((xx, yy, direction))
    return newBlizzard


def printMap(walls, blizzards):
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (x, y) in walls:
                print('#', end='')
                continue

            if (x, y) == pos:
                print('x', end='')
                continue

            cnt = 0
            blizzardChar = None
            if (x, y, NORTH) in blizzards:
                blizzardChar = NORTH
                cnt += 1
            if (x, y, SOUTH) in blizzards:
                blizzardChar = SOUTH
                cnt += 1
            if (x, y, EAST) in blizzards:
                blizzardChar = EAST
                cnt += 1
            if (x, y, WEST) in blizzards:
                blizzardChar = WEST
                cnt += 1

            if cnt == 1:
                print(blizzardChar, end='')
            elif cnt > 1:
                print(cnt, end='')
            else:
                print('.', end='')
        print('')
    print('')


def frozenBlizzard(blizzards):
    return frozenset(blizzards)


start, goal, walls, blizzards = generateMap(lines)
initialB = frozenBlizzard(blizzards)

bstates = []
fblizzards = initialB
while len(bstates) < 2 or fblizzards != initialB:
    # print(len(bstates) + 1)
    fblizzards = frozenBlizzard(nextBlizzardState(walls, fblizzards))
    # printMap(walls, fblizzards)
    bstates.append(fblizzards)


badPos = []
for blizz in bstates:
    bp = set()
    for x, y, direction in blizz:
        bp.add((x, y))
    badPos.append(frozenset(bp))


i = 0
j = 0
# visited = set()
state = (-1, start)
queue = [start]
# visited.add((-1 % len(badPos), start))
while True:
    print(j)
    i %= len(badPos)

    if goal in queue:
        break

    nextQueue = []
    for pos in queue:
        x, y = pos
        candidates = [
             (x, y),
             (x + 1, y),
             (x - 1, y),
             (x, y + 1),
             (x, y - 1),
        ]
        for x, y in candidates:
            if x < 0 or (x, y) in walls:
                continue
            if (x, y) not in badPos[i]:
                nextQueue.append((x, y))

    queue = set(nextQueue)

    i += 1
    j += 1
