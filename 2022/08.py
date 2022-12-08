import utils
import numpy as np

# from sortedcontainers import *

utils.DEBUG = True
utils.DEBUG = False
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
# inputLines = utils.fileToString(utils.inputFilePath())
itemsList = utils.linesToChars(inputLines)
itemsList = [[int(item) for item in row] for row in itemsList]
#
# print(utils.linesToNumbers(inputLines))
# print(utils.digitsInString(inputLines))

treeMap = np.array(itemsList)

maxY = len(itemsList)
maxX = len(itemsList[0])

print(treeMap)

dirToVector = {
    'r': (1, 0),
    'l': (-1, 0),
    'd': (0, 1),
    'u': (0, -1)
}


def getBordersAndDirection(_m):
    b = []
    for i in range(maxY):
        b.append((0, i, -1, 'r'))
        b.append((maxX - 1, i, -1, 'l'))
    for i in range(maxX):
        b.append((i, 0, -1, 'd'))
        b.append((i, maxX - 1, -1, 'u'))
    return b


def get(_m, _x, _y):
    return _m[_y, _x] if 0 <= _x < maxX and 0 <= _y < maxY else None


exploring = getBordersAndDirection(treeMap)
visible = []
while len(exploring) > 0:
    nextExploring = []
    for x, y, maxHeight, direction in exploring:
        nextMax = maxHeight
        newHeight = get(treeMap, x, y)
        if newHeight is None:
            continue
        if newHeight > maxHeight:
            nextMax = newHeight
            visible.append((x, y))

        u, v = dirToVector[direction]
        nextExploring.append((x + u, y + v, nextMax, direction))
    exploring = nextExploring

visible = set(visible)
print(len(visible))

allTrees = set([(i, j) for i in range(maxX) for j in range(maxY)])

scoresSum = {}
for tree in allTrees:
    x, y = tree
    scores = {
        'r': 0,
        'l': 0,
        'u': 0,
        'd': 0,
    }
    for direction, vect in dirToVector.items():
        u, v = vect
        score = 0
        treeHeight = get(treeMap, x, y)
        posX, posY = x, y
        while True:
            posX += u
            posY += v
            height = get(treeMap, posX, posY)
            if height is None or height >= treeHeight:
                if height is not None:
                    score += 1
                break
            score += 1
        scores[direction] = score
    scoresSum[(x, y)] = scores['r'] * scores['l'] * scores['u'] * scores['d']

scoresSumMax = list(scoresSum.values())
scoresSumMax.sort()
print(scoresSumMax[-1])
