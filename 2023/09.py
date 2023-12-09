import utils
import itertools
from math import lcm

# utils.DEBUG = True
utils.printInfo()

data = utils.fileToLString(utils.inputFilePath()).split('\n')
data = map(lambda x: list(map(int, x.split(' '))), data)
data = list(data)

def isAllN(l, n):
    for x in l:
        if x != n:
            return False
    return True

assert(isAllN([1,1,1], 1))
assert(not isAllN([1,1,1], 0))
assert(not isAllN([1,1,0], 1))
assert(not isAllN([1,1,0], 0))
assert(isAllN([], 0))

def buildPyramid(line):
    pyramid = []
    currentLine = [x for x in line]
    
    while not isAllN(currentLine, 0):
        c = []
        for i, x1 in enumerate(currentLine):
            if i == len(currentLine) - 1:
                continue
            x2 = currentLine[i + 1]
            c.append(x2 - x1)
        pyramid.append(currentLine)
        currentLine = c
    
    pyramid.append(currentLine)
    # print(pyramid)
    return pyramid


# Part 1
interpolates = []
for line in data:
    pyramid = buildPyramid(line)

    placeholders = []
    for line in reversed(pyramid):
        if len(placeholders) == 0:
            placeholders.append(0)
            continue

        lastP = placeholders[-1]
        nextP = lastP + line[-1]
        placeholders.append(nextP)

    # print(placeholders)
    interpolate = placeholders[-1]
    interpolates.append(interpolate)

print(sum(interpolates))

# Part 2
interpolates = []
for line in data:
    pyramid = buildPyramid(line)

    placeholders = []
    for line in reversed(pyramid):
        if len(placeholders) == 0:
            placeholders.append(0)
            continue

        lastP = placeholders[-1]
        nextP = line[0] - lastP
        placeholders.append(nextP)

    # print(placeholders)
    interpolate = placeholders[-1]
    interpolates.append(interpolate)

print(sum(interpolates))
