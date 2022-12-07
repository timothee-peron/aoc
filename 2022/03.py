import utils

# import numpy as np
# from sortedcontainers import *

utils.DEBUG = True
utils.DEBUG = False
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
itemsList = utils.linesToChars(inputLines)
# utils.linesToNumbers(inputLines)
# utils.digitsInString(inputLines)


splitlists = [(A[:len(A) // 2], A[len(A) // 2:]) for A in itemsList]
itemsets = [(set(A[:len(A) // 2]), set(A[len(A) // 2:])) for A in itemsList]
itemsetsInter = [list(set(A[:len(A) // 2]).intersection(set(A[len(A) // 2:])))[0] for A in itemsList]


def scoreOfLetter(l):
    score = ord(l) - ord('a')
    if (score < 0):
        score = ord(l) - ord('A') + 26
    return score + 1


itemsetsInterScore = list(map(scoreOfLetter, itemsetsInter))

print(sum(itemsetsInterScore))

subgroups = list(zip(*(iter(itemsList),) * 3))
subgroups = utils.groupListByN(itemsList, 3)

subgroupsSets = [list(set(x[0]).intersection(set(x[1])).intersection(set(x[2])))[0] for x in subgroups]
subgroupsSetsInterScore = list(map(scoreOfLetter, subgroupsSets))

print(sum(subgroupsSetsInterScore))
