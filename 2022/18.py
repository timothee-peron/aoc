from queue import Queue
from itertools import permutations
import math

import utils
import numpy as np

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
# wholFile = utils.fileToLString(utils.inputFilePath())
inputLines = [list(map(int, x.split(','))) for x in inputLines]
print(inputLines)

# ( direction: x=0 y=1 z=2 , x , y , z ) of face
X = 1
Y = 2
Z = 3
exposedFaces = set()
hiddenFaces = set()
for x, y, z in inputLines:
    faces = [(X, x, y, z),
             (Y, x, y, z),
             (Z, x, y, z),
             (X, x + 1, y, z),
             (Y, x, y + 1, z),
             (Z, x, y, z + 1)]
    for face in faces:
        if face in exposedFaces:
            exposedFaces.discard(face)
            hiddenFaces.add(face)
        else:
            exposedFaces.add(face)

print("Part1")
print(len(exposedFaces))


# part 2

def closed_range(start, stop, step=1):
    dir = 1 if (step > 0) else -1
    return list(range(start, stop + dir, step))


coords = list(zip(*inputLines))
neg = (min(coords[0]) - 1, min(coords[1]) - 1, min(coords[2]) - 1)
pos = (max(coords[0]) + 1, max(coords[1]) + 1, max(coords[2]) + 1)

#
# 1  | z = 2
# y  |
# \  |
#  \ |
#   \|-----------> x = 0

steam = [(0, 0, 0)]
visited = set()
trueOuter = set()
while len(steam) > 0:
    newSteam = []
    for x, y, z in steam:
        visited.add((x, y, z))

    for x, y, z in steam:
        relatedSurfaces = [
            (X, x + 1, y, z),
            (X, x, y, z),
            (Y, x, y + 1, z),
            (Y, x, y, z),
            (Z, x, y, z + 1),
            (Z, x, y, z)
        ]
        for sur in relatedSurfaces:
            if sur in exposedFaces:
                trueOuter.add(sur)
                continue
            ds, xs, ys, zs = sur
            nextSteam = (
                x + (0 if ds != X else (-1 if xs == x else 1)),
                y + (0 if ds != Y else (-1 if ys == y else 1)),
                z + (0 if ds != Z else (-1 if zs == z else 1))
            )
            if nextSteam not in visited \
                    and neg[0] <= nextSteam[0] <= pos[0] \
                    and neg[1] <= nextSteam[1] <= pos[1] \
                    and neg[2] <= nextSteam[2] <= pos[2]:
                newSteam.append(nextSteam)
    steam = list(set(newSteam))

print(len(trueOuter))
