import utils

from functools import reduce

utils.DEBUG = True
utils.DEBUG = False
utils.printInfo()

inputLines = utils.linesToItems(utils.fileToLines(utils.inputFilePath()), list)

m = inputLines
h = len(inputLines)
w = len(inputLines[0])

tree = 0
x = 0
for y in range(h):
    if m[y][x] == '#':
        tree += 1
    x += 3
    x %= w
print(tree)

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
hits = []
for slope in slopes:
    tree = 0
    x = 0
    y = 0
    while y < h:
        if m[y][x] == '#':
            tree += 1
        x += slope[0]
        x %= w
        y+=slope[1]
    hits.append(tree)
result = reduce((lambda x,y: x*y), hits)
print(result)
