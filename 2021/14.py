from collections import Counter
from collections import defaultdict

import numpy as np
import utils

# utils.DEBUG = True
inputFileFullDir = utils.inputFilePath()


def readInputFile(filePath):
    return open(filePath, 'r').read()


_file = readInputFile(inputFileFullDir).split('\n\n')

template = list(_file[0])
instructions = _file[1].split('\n')
instructions = [list(i) for i in instructions]
instructions = [(i[0], i[1], i[6]) for i in instructions]

emptyStr = ""

# STEP 1
i = 0
print(f"Step {i}: {emptyStr.join(template)}")
for i in range(10):
    stack = []
    j = 0
    _template = []
    for letter in template:
        stack.append(letter)
        if len(stack) < 2:
            continue
        if len(stack) > 2:
            stack.pop(0)
        j += 1

        _template.append(stack[0])

        for instruction in instructions:
            a, b, insert = instruction
            if stack[0] == a and stack[1] == b:
                _template.append(insert)
                j += 1
    lastLetter = template[-1]
    template = _template
    template.append(lastLetter)
    print(f"Step {i + 1}: {emptyStr.join(template)}")

tCounter = Counter(template)
print(tCounter)
tCountVals = list(tCounter.values())
tCountVals.sort()

print(tCountVals[-1] - tCountVals[0])

# STEP 2
template = list(_file[0])
templatePairs = [(template[i], template[i + 1]) for i in range(len(template) - 1)]

templatePairsCount = Counter(templatePairs)

print(templatePairsCount)

for i in range(40):
    _templatePairsCount = templatePairsCount.copy()
    for instruction in instructions:
        a, b, insert = instruction
        for x, y in templatePairsCount.keys():
            if x == a and y == b:
                # if (x, insert) not in _templatePairsCount:
                #    _templatePairsCount[(x, insert)] = 0
                _templatePairsCount[(x, insert)] += templatePairsCount[(x, y)]
                # if (insert, y) not in _templatePairsCount:
                #    _templatePairsCount[(insert, y)] = 0
                _templatePairsCount[(insert, y)] += templatePairsCount[(x, y)]
                _templatePairsCount[(x, y)] -= templatePairsCount[(x, y)]
    templatePairsCount = _templatePairsCount
    print(f"Step {i + 1}: ", end='')
    print(templatePairsCount)

lettersCount = defaultdict(lambda: 0)
for k, v in templatePairsCount.items():
    a, b = k
    lettersCount[a] += v
lettersCount[template[-1]] += 1

print(lettersCount)

tCountVals = list(lettersCount.values())
tCountVals.sort()
print(tCountVals[-1] - tCountVals[0])
