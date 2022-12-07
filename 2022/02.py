import utils

# import numpy as np
# from sortedcontainers import *

utils.DEBUG = True
utils.DEBUG = False
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
inp = utils.linesToChars(inputLines)

cardScore = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}

# 3
draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

# 6
win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

# 0
loose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}

sc = {
    'l': 0,
    'd': 3,
    "w": 6
}

print(inp)
score = 0


def gameToPlays(g):
    return g[0], g[2]


def scoreOfCard(c):
    return cardScore.get(c)


def getStatusGame(a, x):
    if win.get(a) == x:
        return 'w'
    if loose.get(a) == x:
        return 'l'
    if draw.get(a) == x:
        return 'd'


def scoreOfGame(a, x):
    return scoreOfCard(x) + sc.get(getStatusGame(a, x))


total = 0

for line in inp:
    (a, x) = gameToPlays(line)
    total += scoreOfGame(a, x)

print(total)

wanted = {
    'X': 'l',
    'Y': 'd',
    "Z": 'w'
}


def getWantedStatus(x):
    return wanted.get(x)


def getWantedCard(a, stat):
    if stat == 'w':
        return win.get(a)
    if stat == 'l':
        return loose.get(a)
    if stat == 'd':
        return draw.get(a)


total = 0

for line in inp:
    (a, x) = gameToPlays(line)
    status = getWantedStatus(x)
    card2 = getWantedCard(a, status)
    total += scoreOfGame(a, card2)

print(total)

# print(utils.digitsInString("aaa1-10aaa99999"))
