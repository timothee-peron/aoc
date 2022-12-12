import utils
from collections import defaultdict
import numpy as np

# from sortedcontainers import *

utils.DEBUG = True
utils.DEBUG = False
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
wholeFile = utils.fileToLString(utils.inputFilePath())

start = (-1, -1)
goal = (-1, -1)
mapMatrix = []
startsPart2 = set()
for y, line in enumerate(inputLines):
    row = []
    for x, c in enumerate(line):
        char = c
        if c == 'S':
            start = (x, y)
            char = 'a'
        if c == 'E':
            goal = (x, y)
            char = 'z'
        height = ord(char) - ord('a')
        if height == 0:
            startsPart2.add((x, y))
        row.append(height)
    mapMatrix.append(row)

maxY = len(mapMatrix)
maxX = len(mapMatrix[0])

mapMatrix = np.array(mapMatrix)


# print(mapMatrix)


def getNeighbors(_m, coords):
    _maxY = len(_m)
    _maxX = len(_m[0])
    x, y = coords
    n = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    r = []
    for _x, _y in n:
        if 0 <= _x < _maxX and 0 <= _y < _maxY:
            if _m[_y, _x] <= _m[y, x] + 1:
                r.append((_x, _y))
    return r


# printMatrix(riskMatrix)
def dijskstra(riskMatrix, start):
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
    score = {start: 0}
    queue = {start: 0}
    i = 0
    while len(queue) > 0:
        selectedNode = min(queue, key=queue.get)
        selectedDist = queue[selectedNode]
        score[selectedNode] = queue[selectedNode]
        queue.pop(selectedNode)
        for neighbor in getNeighbors(riskMatrix, selectedNode):
            # altDist = selectedDist + edges[(selectedNode, neighbor)]
            altDist = selectedDist + 1
            if (neighbor not in queue and neighbor not in score) or (neighbor in queue and altDist < queue[neighbor]):
                queue[neighbor] = altDist
                ancestors[neighbor] = selectedNode

    return score, ancestors


score, ancestors = dijskstra(mapMatrix, start)
lastCoord = goal
path = [goal]
while path[-1] != start:
    path.append(ancestors[path[-1]])
path.reverse()
# print(path)

print("part1")
print(score[lastCoord])

scores = set()
# print(startsPart2)
for coords in startsPart2:
    score, ancestors = dijskstra(mapMatrix, coords)
    lastCoord = goal
    # path = [goal]
    # while path[-1] != start:
    #     path.append(ancestors[path[-1]])
    # path.reverse()
    # print(path)
    if lastCoord in score:
        scores.add(score[lastCoord])

print("part2")
print("slow but works!")
print(min(scores))
