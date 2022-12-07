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

stacksInput = []
instructionsInput = []

mode = 0
for line in inputLines:
    if line == "":
        mode = 1
        continue

    if mode == 0:
        stacksInput.append(list(line))

    if mode == 1:
        instructionsInput.append(line.split(' '))

# print(stacksInput)

maxlen = max(map(lambda x: len(x), stacksInput))
for line in stacksInput:
    while len(line) < maxlen:
        line.append('')

initStacks = np.array(stacksInput)
stacksMatrix = np.transpose(initStacks)
stacks = stacksMatrix.tolist()


def getStackDict(stacks):
    realStacks = {}
    for stack in stacks:
        realStack = []
        for letter in stack:
            if letter != '' and letter != '[' and letter != ']' and letter != ' ':
                realStack.append(letter)

        if len(realStack) == 0:
            continue

        stack = realStack[:-1]
        stack.reverse()
        realStacks[realStack[-1]] = stack

    return realStacks


realStacks = getStackDict(stacks)

print(realStacks)
print(instructionsInput)


def applyInstructions(stacks, instructions):
    for instruction in instructions:
        moveFrom = instruction[3]
        moveTo = instruction[5]
        moveNum = instruction[1]

        for i in range(int(moveNum)):
            crate = stacks[moveFrom].pop()
            stacks[moveTo].append(crate)


def applyInstructions2(stacks, instructions):
    for instruction in instructions:
        moveFrom = instruction[3]
        moveTo = instruction[5]
        moveNum = instruction[1]

        moved = []
        for i in range(int(moveNum)):
            crate = stacks[moveFrom].pop()
            moved.append(crate)
        moved.reverse()
        for crate in moved:
            stacks[moveTo].append(crate)


def getTopCrates(stacks):
    word = ""
    for v in stacks.values():
        word = word + v[-1]
    return word


applyInstructions(realStacks, instructionsInput)

word = getTopCrates(realStacks)

print(realStacks)
print(word)

realStacks = getStackDict(stacks)
applyInstructions2(realStacks, instructionsInput)
word = getTopCrates(realStacks)
print(realStacks)
print(word)
