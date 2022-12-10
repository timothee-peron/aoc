import utils
import numpy as np
from collections import Counter

utils.DEBUG = True
utils.DEBUG = False

inputLines = utils.fileToLines(utils.inputFilePath())
wholeFile = utils.fileToLString(utils.inputFilePath())

inputLines = [[int(i) for i in line] for line in inputLines]

matrix = np.array(inputLines)
matrixT = matrix.T

gamma = []
epsilon = []
for bitNumber in matrixT:
    count = Counter(bitNumber)
    gamma.append(max(count, key=count.get))
    epsilon.append(min(count, key=count.get))

gammaS = ''.join(str(x) for x in gamma)
epsilonS = ''.join(str(x) for x in epsilon)

gammaD = int(gammaS, 2)
epsilonD = int(epsilonS, 2)

print("step 1")
print(gammaD * epsilonD)

candidatesO2 = [[int(i) for i in line] for line in inputLines]
candidatesCo2 = [[int(i) for i in line] for line in inputLines]

i = 0
while len(candidatesO2) > 1:
    matrix = np.array(candidatesO2)
    matrixT = matrix.T
    bitNumber = matrixT[i]

    count = Counter(bitNumber)
    criteria = max(count, key=count.get) if count[0] != count[1] else 1

    flagToRemove = []
    for candidate in candidatesO2:
        if candidate[i] != criteria:
            flagToRemove.append(candidate)

    for c in flagToRemove:
        candidatesO2.remove(c)

    i += 1

i = 0
while len(candidatesCo2) > 1:
    matrix = np.array(candidatesCo2)
    matrixT = matrix.T
    bitNumber = matrixT[i]

    count = Counter(bitNumber)
    criteria = min(count, key=count.get) if count[0] != count[1] else 0

    flagToRemove = []
    for candidate in candidatesCo2:
        if candidate[i] != criteria:
            flagToRemove.append(candidate)

    for c in flagToRemove:
        candidatesCo2.remove(c)

    i += 1

candidatesO2S = ''.join(str(x) for x in candidatesO2[0])
candidatesCo2S = ''.join(str(x) for x in candidatesCo2[0])

candidatesO2D = int(candidatesO2S, 2)
candidatesCo2D = int(candidatesCo2S, 2)

print("step 2")
print(candidatesO2D * candidatesCo2D)
