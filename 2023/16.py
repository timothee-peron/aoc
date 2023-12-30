import utils
from functools import cache

# utils.DEBUG = True
utils.printInfo()

data = list(map(list, utils.fileToLString(utils.inputFilePath()).strip().split('\n')))

H, W = len(data), len(data[0])

def printMap(_data, posList):
    print('')
    for y, row in enumerate(_data):
        for x, c in enumerate(row):
            if (x, y) in posList:
                print('#', end='')
            else:
                print(c, end='')
        print('')
    print('')

def checkP(_pos):
    x, y = _pos
    return True if 0 <= x < W and 0 <= y < H else False

def addCoord(a, b):
    return (a[0] + b[0], a[1] + b[1])

def getBeams(char, dir, pos):
    if char == '.':
        return [(dir, addCoord(dir, pos))]
    if dir[0] == 0 and char == '|':
        return [(dir, addCoord(dir, pos))]
    if dir[1] == 0 and char == '-':
        return [(dir, addCoord(dir, pos))]
    if char == '|':
        return [((0, 1), addCoord(pos, (0, 1))), ((0, -1), addCoord(pos, (0, -1)))]
    if char == '-':
        return [((1, 0), addCoord(pos, (1, 0))), ((-1, 0), addCoord(pos, (-1, 0)))]
    if char == '/':
        if dir == (1, 0):
            v = (0, -1)
        if dir == (-1, 0):
            v = (0, 1)
        if dir == (0, 1):
            v = (-1, 0)
        if dir == (0, -1):
            v = (1, 0)
        return [(v, addCoord(v, pos))]
    if char == '\\':
        if dir == (1, 0):
            v = (0, 1)
        if dir == (-1, 0):
            v = (0, -1)
        if dir == (0, 1):
            v = (1, 0)
        if dir == (0, -1):
            v = (-1, 0)
        return [(v, addCoord(v, pos))]

def computeVisited(start):
    visited = set()
    visitedWdir = set()

    
    # list of direction position
    # beams = [((1, 0), (0, 0))]
    beams = start

    while len(beams) > 0:
        todo = [x for x in beams]
        beams = []

        # printMap(data, visited)

        for direction, pos in todo:
            visited.add(pos)
            visitedWdir.add((pos, direction))
            x, y = pos
            c = data[y][x]

            for dir2, pos2 in getBeams(c, direction, pos):
                if not checkP(pos2):
                    continue

                if (pos2, dir2) in visitedWdir:
                    continue
                beams.append((dir2, pos2))
    return visited

# part 1
print(len(computeVisited([((1, 0), (0, 0))])))

starts = []
for x in range(W):
    starts.append(((0, 1), (x, 0)))
    starts.append(((0, -1), (x, H-1)))
for y in range(H):
    starts.append(((1, 0), (0, y)))
    starts.append(((-1, 0), (W-1, y)))

count = []
for s in starts:
    count.append(len(computeVisited([s])))

print(max(count))
