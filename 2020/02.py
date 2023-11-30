import utils

from collections import Counter

utils.DEBUG = True
utils.DEBUG = False
utils.printInfo()

inputLines = utils.linesToItems(utils.fileToLines(utils.inputFilePath()), lambda l: l.split(': '))
inputLines = [(l[0].split(' ')[0], l[0].split(' ')[1], l[1]) for l in inputLines]
inputLines = [(int(l[0].split('-')[0]), int(l[0].split('-')[1]), l[1], l[2]) for l in inputLines]

matches = 0
for a,b,c,d in inputLines:
    chars = list(d)
    e = Counter(chars)
    if a <= e[c] <= b:
        matches += 1
print(matches)

matches = 0
for a,b,c,d in inputLines:
    chars = list(d)
    chars = [chars[a-1], chars[b-1]]
    e = Counter(chars)
    if e[c] == 1:
        matches += 1
print(matches)
