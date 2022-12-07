import os

inputFileDir = os.path.dirname(__file__)
inputFileName = "sample.txt"
inputFileName = "input.txt"

inputFileFullDir = os.path.join(inputFileDir, inputFileName)


def readInputFile(filePath):
    return open(filePath, 'r').read().splitlines()


def convertToMatrix(lines):
    rows = []
    for line in lines:
        letters = list(line)
        digits = list(map(lambda x: int(x), letters))
        rows.append(digits)
    return rows


def getM(m, x, y):
    return m[y][x]


def setM(m, x, y, val):
    m[y][x] = val


def increaseByN(m, x, y, n):
    setM(m, x, y, getM(m, x, y) + n)


def increaseAllByN(m, n):
    for y in range(len(m)):
        for x in range(len(m[y])):
            increaseByN(m, x, y, n)


def isValidCoords(m, x, y):
    if 0 <= x < len(m[0]) and 0 <= y < len(m):
        return True
    return False


def getAdjacentCoords(m, x, y):
    adj = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y),
           (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1), ]
    return list(filter(lambda c: isValidCoords(m, c[0], c[1]), adj))


def findCoordsAboveN(m, n):
    coords = []
    for y in range(len(m)):
        for x in range(len(m[y])):
            val = getM(m, x, y)
            if val > n:
                coords.append((x, y))
    return coords


def resetFlashed(m):
    flashing = set(findCoordsAboveN(m, 9))
    for x, y in flashing:
        setM(m, x, y, 0)


def step(m):
    increaseAllByN(m, 1)
    flashList = set()
    flashing = set(findCoordsAboveN(m, 9))
    for flash in flashing:
        flashList.add(flash)
    while len(flashing) > 0:
        impactedAdj = {}
        for x, y in flashing:
            adjs = getAdjacentCoords(m, x, y)
            for adj in adjs:
                if adj not in impactedAdj.keys():
                    impactedAdj[adj] = 0
                impactedAdj[adj] = 1 + impactedAdj[adj]
        for coords, val in impactedAdj.items():
            (x, y) = coords
            increaseByN(m, x, y, val)
        flashing = set(findCoordsAboveN(m, 9))
        for flashed in flashList:
            flashing.discard(flashed)
        for flash in flashing:
            flashList.add(flash)
    printMatrix(matrix)
    resetFlashed(m)
    return len(flashList)


def printMatrix(m):
    print('################"')
    for row in m:
        for c in row:
            print(c if c < 10 else "*", end='')
        print('')
    print('################"')
    print('')


inputLines = readInputFile(inputFileName)
matrix = convertToMatrix(inputLines)

ctn = 0
for i in range(100):
    print(f"step {i}")
    ctn += step(matrix)

print(ctn)


def step2(m):
    increaseAllByN(m, 1)
    flashList = set()
    flashing = set(findCoordsAboveN(m, 9))
    for flash in flashing:
        flashList.add(flash)
    while len(flashing) > 0:
        impactedAdj = {}
        for x, y in flashing:
            adjs = getAdjacentCoords(m, x, y)
            for adj in adjs:
                if adj not in impactedAdj.keys():
                    impactedAdj[adj] = 0
                impactedAdj[adj] = 1 + impactedAdj[adj]
        for coords, val in impactedAdj.items():
            (x, y) = coords
            increaseByN(m, x, y, val)
        flashing = set(findCoordsAboveN(m, 9))
        for flashed in flashList:
            flashing.discard(flashed)
        for flash in flashing:
            flashList.add(flash)
    # printMatrix(matrix)
    allFlash = len(set(findCoordsAboveN(m, 9))) == len(m) * len(m[0])
    resetFlashed(m)
    return allFlash


matrix2 = convertToMatrix(inputLines)
i = 0
while True:
    i += 1
    print(f"step {i}")
    allFlash = step2(matrix2)
    if allFlash:
        print("ALL FLASHED")
        break
