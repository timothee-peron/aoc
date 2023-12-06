import numpy as np
import utils

# utils.DEBUG = True

inputLines = utils.fileToLines(utils.inputFilePath())
wholeFile = utils.fileToLString(utils.inputFilePath())

riskMatrix = [[int(x) for x in line] for line in inputLines]

maxY = len(riskMatrix)
maxX = len(riskMatrix[0])

riskMatrix = np.array(riskMatrix)


def printMatrix(_m):
    print('-' * maxX)
    for line in _m:
        for i in line:
            print(i, end='')
        print('')


def getNeighbors(_m, coords):
    _maxY = len(_m)
    _maxX = len(_m[0])
    x, y = coords
    n = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    r = []
    for x, y in n:
        if 0 <= x < _maxX and 0 <= y < _maxY:
            r.append((x, y))
    return r


# printMatrix(riskMatrix)
def dijskstra(riskMatrix):
    maxY = len(riskMatrix)
    maxX = len(riskMatrix[0])

    nodes = set()
    for y in range(maxY):
        for x in range(maxX):
            nodes.add((x, y))

    ancestors = {}

    edges = {}
    for node in nodes:
        ns = getNeighbors(riskMatrix, node)
        for n in ns:
            edges[(node, n)] = riskMatrix[n[1], n[0]]

    # Dijkstra
    score = {(0, 0): 0}
    queue = {(0, 0): 0}
    i = 0
    while len(queue) > 0:
        # print(queue)
        selectedNode = min(queue, key=queue.get)
        selectedDist = queue[selectedNode]
        score[selectedNode] = queue[selectedNode]
        queue.pop(selectedNode)
        for neighbor in getNeighbors(riskMatrix, selectedNode):
            # altDist = selectedDist + edges[(selectedNode, neighbor)]
            altDist = selectedDist + riskMatrix[neighbor[1], neighbor[0]]
            if (neighbor not in queue and neighbor not in score) or (neighbor in queue and altDist < queue[neighbor]):
                queue[neighbor] = altDist
                ancestors[neighbor] = selectedNode

    return score, ancestors


score, ancestors = dijskstra(riskMatrix)
lastCoord = (maxX - 1, maxY - 1)
path = [lastCoord]
while path[-1] != (0, 0):
    path.append(ancestors[path[-1]])
path.reverse()
print(path)

print("part1")
print(score[lastCoord])

# PART 2

riskMatrix = [[int(x) for x in line] for line in inputLines]
maxY = len(riskMatrix)
maxX = len(riskMatrix[0])

bigMatrix = []
for y in range(5 * maxY):
    row = []
    for x in range(5 * maxX):
        delta = (x // maxX) + (y // maxY)
        row.append(((riskMatrix[y % maxY][x % maxX] + delta - 1) % 9) + 1)
    bigMatrix.append(row)

maxY = len(bigMatrix)
maxX = len(bigMatrix[0])

bigMatrix = np.array(bigMatrix)

score, ancestors = dijskstra(bigMatrix)
lastCoord = (maxX - 1, maxY - 1)
path = [lastCoord]
while path[-1] != (0, 0):
    path.append(ancestors[path[-1]])
path.reverse()
print(path)

print("part2")
print(score[lastCoord])
