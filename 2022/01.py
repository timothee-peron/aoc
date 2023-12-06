import utils

# import numpy as np
# from sortedcontainers import *

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())

cals = []
current = []
for cal in inputLines:
    if cal == '':
        cals.append(current)
        current = []
    else:
        current.append(int(cal))

calsSum = list(map(sum, cals))
print(max(calsSum))

calsSum.sort(reverse=True)
print(calsSum[0] + calsSum[1] + calsSum[2])

# print(utils.digitsInString("aaa1-10aaa99999"))
