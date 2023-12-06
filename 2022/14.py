import math

import utils
import numpy as np

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())

AIR = 0
ROCK = 1
SAND = 2
VOID = -1


def generateMapPaths(lines):
    paths = []
    for line in lines:
        coords = line.split(" -> ")
        path = []
        for coord in coords:
            x, y = coord.split(',')
            path.append((int(x), int(y)))
        paths.append(path)
    return paths


# dirty but voidmargin allows to specify an extremely big matrix for infinite floor
def computeMatrixSize(paths, voidmargin=0):
    minX = paths[0][0][0]
    maxX = paths[0][0][0]
    maxY = paths[0][0][1]
    for path in paths:
        for x, y in path:
            if x < minX:
                minX = x
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y

    return minX - 2 - voidmargin, maxX + 3 + voidmargin, 0, maxY + 3


def getValue(_m, size, coords):
    x, y = coords
    (minX, maxX, minY, maxY) = size
    if not (minX <= x < maxX and minY <= y < maxY):
        return VOID
    return _m[y, x - minX]


def setValue(_m, size, coords, value):
    x, y = coords
    (minX, maxX, minY, maxY) = size
    _m[y, x - minX] = value


def generateMap(paths, size, floor=False):
    (minX, maxX, minY, maxY) = size
    matrix = np.zeros((maxY - minY, maxX - minX))

    for path in paths:
        stack = []
        for point in path:
            stack.append(point)
            if len(stack) > 2:
                stack.pop(0)
            if len(stack) < 2:
                continue

            a, b = stack[0]
            u, v = stack[1][0] - a, stack[1][1] - b
            du, dv = np.sign(u), np.sign(v)

            x, y = a, b
            for i in range(abs(u) + abs(v) + 1):
                setValue(matrix, size, (x, y), ROCK)
                x += du
                y += dv

    if floor:
        x = minX
        while x < maxX:
            setValue(matrix, size, (x, maxY - minY - 1), ROCK)
            x += 1

    return matrix


# returns True if success, False if fall in abyss
def pourSand(position, matrix, size, throwOnVoid=False):
    (minX, maxX, minY, maxY) = size
    x, y = position
    if getValue(matrix, size, (x, y)) != AIR:
        return False

    while True:
        nx, ny = x, y

        below = getValue(matrix, size, (nx, ny + 1))
        belowLeft = getValue(matrix, size, (nx - 1, ny + 1))
        belowRight = getValue(matrix, size, (nx + 1, ny + 1))

        if below == VOID:
            if throwOnVoid:
                raise Exception("VOID ENCOUNTERED!")
            return False

        if below == AIR:
            y += 1
            continue

        if belowLeft == AIR:
            x, y = nx - 1, ny + 1
            continue

        if belowRight == AIR:
            x, y = nx + 1, ny + 1
            continue

        if throwOnVoid and (belowLeft == VOID or belowLeft == VOID):
            raise Exception("VOID ENCOUNTERED!")

        break

    setValue(matrix, size, (x, y), SAND)
    return True


paths = generateMapPaths(inputLines)
size = computeMatrixSize(paths)
matrixMap = generateMap(paths, size)

while True:
    pouring = pourSand((500, 0), matrixMap, size)
    if not pouring:
        break

print("PART1")
count = (matrixMap == 2).sum()
print(count)

print("PART2")
size = computeMatrixSize(paths, 1000)
matrixMap = generateMap(paths, size, True)
while True:
    pouring = pourSand((500, 0), matrixMap, size, throwOnVoid=True)
    if not pouring:
        break
count = (matrixMap == 2).sum()
print(count)
