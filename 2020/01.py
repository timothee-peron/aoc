import sys

import utils

utils.DEBUG = True
utils.DEBUG = False
utils.printInfo()

inputLines = utils.linesToNumbers(utils.fileToLines(utils.inputFilePath()))
allValues = set(inputLines)

for line in inputLines:
    lookup = 2020 - line
    if lookup in allValues:
        print(lookup * line)
        break


for line in inputLines:
    for line2 in inputLines:
        lookup = 2020 - line - line2
        if lookup in allValues:
            print(lookup * line * line2)
            sys.exit(0)
