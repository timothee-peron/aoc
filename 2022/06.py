import utils

import numpy as np

# from sortedcontainers import *

utils.DEBUG = True
utils.DEBUG = False
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
# itemsList = utils.linesToChars(inputLines)
#
# print(utils.linesToNumbers(inputLines))
# print(utils.digitsInString(inputLines))

for line in inputLines:
    stack = []
    i = 0
    for letter in list(line):
        i += 1
        stack.insert(0, letter)
        if len(stack) > 4:
            stack.pop()

        if len(stack) != 4:
            continue

        if len(set(stack)) == 4:
            print(i)
            break

for line in inputLines:
    stack = []
    i = 0
    for letter in list(line):
        i += 1
        stack.insert(0, letter)
        if len(stack) > 14:
            stack.pop()

        if len(stack) != 14:
            continue

        if len(set(stack)) == 14:
            print(i)
            break
