import utils
import json
from functools import cmp_to_key

utils.DEBUG = True
utils.DEBUG = False
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
wholeFile = utils.fileToLString(utils.inputFilePath())

pairsInput = wholeFile.split("\n\n")
pairsInput = [(pair.split('\n')[0], pair.split('\n')[1]) for pair in pairsInput]


def convertToStacks(_list):
    return json.loads(_list)


def compareStacks(left, right):
    il = 0
    ir = 0

    while True:
        if il >= len(left) and ir >= len(right):
            return None
        if il >= len(left):
            return -1
        if ir >= len(right):
            return 1
        u = left[il]
        v = right[ir]
        if isinstance(u, int) and isinstance(v, int):
            if u == v:
                il += 1
                ir += 1
                continue
            return -1 if u < v else 1
        else:
            # list
            listLeft = [u] if isinstance(u, int) else u
            listRight = [v] if isinstance(v, int) else v
            compared = compareStacks(listLeft, listRight)
            if compared is not None:
                return compared

            il += 1
            ir += 1


s = 0
for i, pair in enumerate(pairsInput):
    l = convertToStacks(pair[0])
    r = convertToStacks(pair[1])
    cpr = compareStacks(l, r)
    assert cpr is not None
    if cpr == -1:  # order ok
        s += i + 1

print("part1")
print(s)

# part2

allLines = list(filter(lambda x: x != "", wholeFile.split("\n")))
allLines.append("[[2]]")
allLines.append("[[6]]")

allLines = list(map(convertToStacks, allLines))
allLines = sorted(allLines, key=cmp_to_key(compareStacks))

print("part2")
pos2 = allLines.index([[2]])
pos6 = allLines.index([[6]])
print(pos2 * pos6)
