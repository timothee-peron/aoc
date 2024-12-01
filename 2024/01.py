import utils
from collections import Counter

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
inputPairs = tuple(tuple(map(int, line.split('   '))) for line in inputLines)

left = [item[0] for item in inputPairs]
right = [item[1] for item in inputPairs]
left.sort()
right.sort()

sortedList = zip(left, right)
print(sum(abs(item[0] - item[1]) for item in sortedList))

left = [item[0] for item in inputPairs]
right = [item[1] for item in inputPairs]
right = Counter(right)

print(sum(item * right[item] for item in left))
