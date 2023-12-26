import utils

# utils.DEBUG = True
utils.printInfo()

data = utils.fileToLString(utils.inputFilePath()).split('\n\n')
data = [[list(y) for y in x.strip().split('\n')] for x in data]

def isRowSymetric(_row, _pairs):
    for i, j in _pairs:
        if _row[i] != _row [j]:
            return False
    return True

def getVerticalAxis(_p):
    W = len(_p[0])
    axis = set(i for i in range(1, W))
    for row in _p:
        for x in frozenset(axis):
            R = range(x) if x <= W // 2 else range(W -x)
            pairs = [ (x - i - 1, x + i) for i in R]
            if not isRowSymetric(row, pairs):
                axis.remove(x)
                continue
    return axis

# part 1
sum = 0
for pattern in data:
    # transpose matrix
    t = [list(x) for x in zip(*pattern)]
    for x in getVerticalAxis(t):
        sum += 100 *x
    for x in getVerticalAxis(pattern):
        sum += x
print(sum)


def countDefect(_row, _pairs):
    d = 0
    for i, j in _pairs:
        if _row[i] != _row [j]:
            d += 1
    return d

def getVerticalAxis2(_p):
    W = len(_p[0])
    axis = set(i for i in range(1, W))
    defectPerAxis = {a: 0 for a in axis}
    for row in _p:
        for x in axis:
            R = range(x) if x <= W // 2 else range(W -x)
            pairs = [ (x - i - 1, x + i) for i in R]
            d = countDefect(row, pairs)
            defectPerAxis[x] += d
    
    return {i[0] for i in defectPerAxis.items() if i[1] == 1}

# part 2
sum = 0
for pattern in data:
    # transpose matrix
    t = [list(x) for x in zip(*pattern)]
    for x in getVerticalAxis2(t):
        sum += 100 *x
    for x in getVerticalAxis2(pattern):
        sum += x
print(sum)
