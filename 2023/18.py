import utils
from math import inf

# utils.DEBUG = True
utils.printInfo()

fp = utils.inputFilePath()
data = list(map(lambda l: l.split(' '), utils.fileToLString(fp).strip().split('\n')))

dirToVect={
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0),
}

def addTuples(u, v):
    x1, y1 = u
    x2, y2 = v
    return (x1 + x2, y1 + y2)

def scalarTuple(k, u):
    x1, y1 = u
    return (k*x1, k*y1)

def findSize(s):
    topLeft = (0, 0)
    bottomRight = (0, 0)
    for x, y in s:
        topLeft = (min(x, topLeft[0]), min(y, topLeft[1]))
        bottomRight = (max(x, bottomRight[0]), max(y, bottomRight[1]))
    return (topLeft, bottomRight)


def printSet(s, mark = set()):
    topLeft, bottomRight = findSize(s)
    for y in range(topLeft[1], bottomRight[1] + 1):
        for x in range(topLeft[0], bottomRight[0] + 1):
            print('x' if (x, y) in mark else '#' if (x, y) in s else '.', end= '')
        print('')

def findInsides(s):
    topLeft, bottomRight = findSize(s)
    insides = set()
    for y in range(topLeft[1], bottomRight[1] + 1):
        xes = []
        for x in range(topLeft[0], bottomRight[0] + 1):
            if (x, y) in s:
                xes.append(x)
        
        if len(xes) == 2:
            if xes[0] + 1 == xes[1]:
                raise Exception('glued 2')
            for x in range(xes[0] + 1, xes[1]):
                insides.add((x, y))
    return insides

# part 1
pos = (0, 0)
digged = set([pos])

# dig
for direction, n, color in data:
    n = int(n)
    for i in range(n):
        pos = addTuples(pos, dirToVect[direction])
        digged.add(pos)

insides = findInsides(digged)
explore = list(insides)
# printSet(digged, set([inside]))

# fill
while explore:
    (x, y) = explore.pop()
    insides.add((x, y))
    
    candidates = [
        addTuples((x, y), dirToVect['U']),
        addTuples((x, y), dirToVect['D']),
        addTuples((x, y), dirToVect['R']),
        addTuples((x, y), dirToVect['L']),
    ]

    for candidate in candidates:
        if candidate not in insides and candidate not in explore and candidate not in digged:
            explore.append(candidate)

p1 = len(insides) + len(digged)
print(p1)

if utils.DEBUG:
    assert(72821 == p1)