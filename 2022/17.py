import math
from queue import Queue
from itertools import permutations

import utils
import numpy as np

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
jets = list(inputLines[0])

width = 7
paddingLeft = 2
paddingBottom = 3

rocks = [[[1, 1, 1, 1]],
         [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
         [[0, 0, 1], [0, 0, 1], [1, 1, 1]],
         [[1], [1], [1], [1]],
         [[1, 1], [1, 1]]]


def newLine(width):
    return [0 for _ in range(width)]


def printTower(lines, fallingCoords=set(), header=""):
    print(header)
    i = len(lines) - 1
    while i >= 0:
        print('|', end="")
        for x, value in enumerate(list(lines[i])):
            print("@" if (x, i) in fallingCoords else "#" if value == 1 else ".", end="")
        print('|')
        i -= 1
    print("+" + "-" * len(lines[0]) + "+")
    print('')


# part1
lines = []
tableSize = 0
towerHeight = 0
currentRock = 0
currentJet = 0
for rockNumber in range(2022):
    currentRock %= len(rocks)
    rock = rocks[currentRock]
    currentRock += 1
    rockH = len(rock)

    # adding lines
    for _ in range(rockH + paddingBottom - tableSize + towerHeight + 1):
        lines.append(newLine(width))

    tableSize = len(lines)

    # add rock
    rockPositions = set()
    startingY = towerHeight + paddingBottom + len(rock) - 1
    for y, row in enumerate(rock):
        for x, value in enumerate(row):
            if value == 1:
                position = (2 + x, startingY - y)
                rockPositions.add(position)

    # printTower(lines, rockPositions, "NEW ROCK")

    while True:
        # move jet
        currentJet %= len(jets)
        jet = jets[currentJet]

        # move
        moveSuccess = True
        newPositions = set()
        for x, y in rockPositions:
            dx = 1 if jet == '>' else -1
            newX = x + dx
            newPositions.add((newX, y))
            if newX < 0 or newX >= width or lines[y][newX] == 1:
                moveSuccess = False

        if moveSuccess:
            rockPositions = newPositions

        # printTower(lines, rockPositions)

        currentJet += 1

        # move down
        moveSuccess = True
        newPositions = set()
        for x, y in rockPositions:
            newPositions.add((x, y - 1))
            if y - 1 < 0 or lines[y - 1][x] == 1:
                moveSuccess = False

        if moveSuccess:
            rockPositions = newPositions
        else:
            ys = set()
            ys.add(towerHeight)
            for x, y in rockPositions:
                lines[y][x] = 1
                ys.add(y + 1)
            towerHeight = max(ys)
            rockPositions = set()

        # printTower(lines, rockPositions)

        if not moveSuccess:
            break

    # printTower(lines, rockPositions, "ROCK STOPPED")

# compare my answer!!
print(3144)
print(towerHeight)

# PART2

lines = []
tableSize = 0
towerHeight = 0
currentRock = 0
currentJet = 0
rockNumber = 0
states = {}
cheated = False
simulatedHeight = 0
maxRock = 1000000000000
while rockNumber < maxRock:
    currentRock %= len(rocks)
    rock = rocks[currentRock]
    currentRock += 1
    rockH = len(rock)

    # adding lines
    for _ in range(rockH + paddingBottom - tableSize + towerHeight + 1):
        lines.append(newLine(width))

    tableSize = len(lines)

    # add rock
    rockPositions = set()
    startingY = towerHeight + paddingBottom + len(rock) - 1
    for y, row in enumerate(rock):
        for x, value in enumerate(row):
            if value == 1:
                position = (2 + x, startingY - y)
                rockPositions.add(position)

    while True:
        # move jet
        currentJet %= len(jets)
        jet = jets[currentJet]

        # move
        moveSuccess = True
        newPositions = set()
        for x, y in rockPositions:
            dx = 1 if jet == '>' else -1
            newX = x + dx
            newPositions.add((newX, y))
            if newX < 0 or newX >= width or lines[y][newX] == 1:
                moveSuccess = False

        if moveSuccess:
            rockPositions = newPositions

        currentJet += 1

        # move down
        moveSuccess = True
        newPositions = set()
        for x, y in rockPositions:
            newPositions.add((x, y - 1))
            if y - 1 < 0 or lines[y - 1][x] == 1:
                moveSuccess = False

        if moveSuccess:
            rockPositions = newPositions
        else:
            ys = set()
            ys.add(towerHeight)
            for x, y in rockPositions:
                lines[y][x] = 1
                ys.add(y + 1)
            towerHeight = max(ys)
            rockPositions = set()

        if not moveSuccess:
            break

    rockNumber += 1

    if not cheated:
        lastLines = lines[-30:]
        _hash = 0
        for line in lastLines:
            for v in line:
                _hash <<= 1
                _hash += v
        _newState = (currentJet, currentRock, _hash)
        if _newState not in states.keys():
            states[(currentJet, currentRock, _hash)] = (towerHeight, rockNumber)
        else:
            cheated = True
            towerHeight1, rockNumber1 = states[_newState]
            towerHeight2, rockNumber2 = towerHeight, rockNumber
            # print(towerHeight1, rockNumber1)
            # print(towerHeight2, rockNumber2)

            deltaHeight = towerHeight2 - towerHeight1
            deltaRock = rockNumber2 - rockNumber1
            
            # iterating takes too much time!
            # while True:
            #     newRockNumber = rockNumber + deltaRock
            #     if not newRockNumber < maxRock:
            #         break
            #     simulatedHeight += deltaHeight
            #     rockNumber = newRockNumber

            factor = ((maxRock - rockNumber) // deltaRock)
            simulatedHeight += deltaHeight * factor
            rockNumber += deltaRock * factor

    # print(rockNumber)

# compare my answer!!
print(1565242165201)
print(towerHeight + simulatedHeight)
