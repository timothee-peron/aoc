import utils

# utils.DEBUG = True
utils.printInfo()

data = utils.fileToLString(utils.inputFilePath()).split('\n')
data = map(list, data)
data = list(data)

H = len(data)
W = len(data[0])

charToDir = {
    '|': {'N', 'S'},
    '-': {'W', 'E'},
    'L': {'N', 'E'},
    'J': {'N', 'W'},
    '7': {'S', 'W'},
    'F': {'S', 'E'},
    '.': set(),
    'S': set(),
}

dirToVect = {
    'N' : (0, -1),
    'S' : (0, 1),
    'W' : (-1, 0),
    'E' : (1, 0),
}

oppositeDir = {
    'N': 'S',
    'S': 'N',
    'W': 'E',
    'E': 'W',
}

def findFirstChar(_c, _data):
    for y, row in enumerate(_data):
        for x, c in enumerate(row):
            if c == _c:
                return (x, y)

def nextNode(V, D):
    Vx, Vy = V
    Ux, Uy = dirToVect[D]
    Wx, Wy = Vx + Ux, Vy + Uy
    ch = data[Wy][Wx]
    dirs = charToDir[ch]
    _follow = list(dirs - {oppositeDir[D]})
    if len(_follow) != 1:
        return ((Wx, Wy), '?')
    return ((Wx, Wy), _follow[0])

# find start coordinates
start = findFirstChar('S', data)
sx, sy = start

# find start + direction
nodes = []
for d, v in dirToVect.items():
    vx, vy = v
    u, w = sx + vx, sy + vy
    if not (0 <= u < W and 0 <= w < H):
        continue
    ch = data[w][u]
    dirs = charToDir[ch]

    if oppositeDir[d] in dirs:
        nodes.append((start, d))

# for part 2
start1 = nodes[0]

# count untill arrive at opposite
i = 0
while i == 0 or nodes[0][0] != nodes[1][0]:
    N0 = nodes[0]
    N1 = nodes[1]
    nodes = []
    nodes.append(nextNode(N0[0], N0[1]))
    nodes.append(nextNode(N1[0], N1[1]))
    i += 1

print(i)

# part 2
allNodes = [start1]
while True:
    lastNode = allNodes[-1]
    _c = data[lastNode[0][1]][lastNode[0][0]]
    if len(allNodes) == 1:
        pass
    elif _c == 'S':
        break
    nextN = nextNode(lastNode[0], lastNode[1])
    allNodes.append(nextN)

allNodes.pop()
perimeter = len(allNodes)

clockWise = ['S', 'W', 'N', 'E', 'S']
cclockWise = ['S', 'E', 'N', 'W', 'S']

permimeterDirs = list(map(lambda x: x[1], allNodes))
permimeterDirs.append(permimeterDirs[0])

totalTurns = 0
for i in range(perimeter):
    d1, d2 = permimeterDirs[i], permimeterDirs[i + 1]
    if d1 == d2:
        continue
    if d2 == clockWise[clockWise.index(d1) + 1]:
        totalTurns += 1
    elif d2 == cclockWise[cclockWise.index(d1) + 1]:
        totalTurns -= 1
    else:
        raise(Exception("Impossible"))

assert(totalTurns == 4 or totalTurns == -4)
isClockWise = totalTurns == 4

# print(isClockWise)

perimeterCoordinates = set(map(lambda x: x[0], allNodes))

toFill = set()
for i, (vect, d) in enumerate(allNodes):
    vx, vy = vect
    ch = data[vy][vx]
    
    _d0 = permimeterDirs[i - 1]
    _d1 = permimeterDirs[i]
    if _d0 == _d1:
        # straight

        # if perimeter is going cclockwise, inside is also ccw
        if isClockWise:
            _orth = clockWise[clockWise.index(_d1) + 1]
        else:
            _orth = cclockWise[cclockWise.index(_d1) + 1]
        ux, uy = dirToVect[_orth]
        insideX, insideY = vx + ux, vy + uy
    else:
        d0x, d0y = dirToVect[_d0]
        d1x, d1y = dirToVect[_d1]

        #corner
        if (_d1 == clockWise[clockWise.index(_d0) + 1] and isClockWise) or \
            (_d1 == cclockWise[cclockWise.index(_d0) + 1] and not isClockWise):
            # same side
            ux, uy = d1x - d0x, d1y - d0y
            insideX, insideY = vx + ux, vy + uy
        else:
            # other side: 3 coordinates!
            ux, uy = d0x - d1x, d0y - d1y
            insideX, insideY = vx + ux, vy + uy
            if (insideX, insideY) not in perimeterCoordinates:
                toFill.add((insideX, insideY))
            ux, uy = - d1x, - d1y
            insideX, insideY = vx + ux, vy + uy
            if (insideX, insideY) not in perimeterCoordinates:
                toFill.add((insideX, insideY))
            ux, uy = d0x, d0y
            insideX, insideY = vx + ux, vy + uy
            if (insideX, insideY) not in perimeterCoordinates:
                toFill.add((insideX, insideY))
            continue

    if (insideX, insideY) not in perimeterCoordinates:
        toFill.add((insideX, insideY))

filled = set(toFill)
while len(toFill) > 0:
    filling = frozenset(toFill)
    toFill = set()
    for _x0, _y0 in filling:
        for _u, _v in dirToVect.values():
            _x, _y = _x0 + _u, _y0 + _v
            if (_x, _y) not in filled and 0 <= _x < W and 0 <= _y < H and (_x, _y) not in perimeterCoordinates:
                toFill.add((_x, _y))
                filled.add((_x, _y))
            

# for y, row in enumerate(data):
#     for x, c in enumerate(row):
#         if (x, y) in filled:
#             print('#', end='')
#         else:
#             print(c, end = '')
#     print('')

print(len(filled))