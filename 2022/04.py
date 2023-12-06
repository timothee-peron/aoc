import utils

# import numpy as np
# from sortedcontainers import *

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
# itemsList = utils.linesToChars(inputLines)
#
# print(utils.linesToNumbers(inputLines))
# print(utils.digitsInString(inputLines))

pairsList = list(map(lambda x: [list(map(lambda z: int(z), y.split('-'))) for y in x.split(',')], inputLines))
print(pairsList)

contains = 0
overlap = 0
for p1, p2 in pairsList:
    print(p1, p2)
    r1 = list(range(p1[0], p1[1] + 1))
    r2 = list(range(p2[0], p2[1] + 1))
    print(r1, r2)
    s1 = set(r1)
    s2 = set(r2)
    if s1.issubset(s2) or s2.issubset(s1):
        contains += 1
    if len(s1.intersection(s2)) > 0:
        overlap += 1

print(contains)
print(overlap)
