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

numToDir = {
    0: 'R',
    1: 'D',
    2: 'L',
    3: 'U',
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

def countInsides(s):
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
vertices=[pos]

# find all vertical dig segments
boundary = 0
for direction, n, color in data:
    n = int(n)
    pos = addTuples(pos, scalarTuple(n, dirToVect[direction]))
    vertices.append(pos)
    boundary += n

# shoelace
area = 0
for i in range(len(vertices)-1):
    x, y= vertices[i]
    xx, yy = vertices[i+1]
    area += -(y+yy)*(x-xx) / 2

p1 = int(area + boundary/2 + 1)
print(p1)

if not utils.DEBUG:
    assert(72821 == p1)
else:
    assert(62 == p1)


# part 2
pos = (0, 0)
vertices=[pos]

# find all vertical dig segments
boundary = 0
for direction, n, color in data:
    instruction = color.split('#')[1]
    n, direction = int('0x'+instruction[0:5], base = 16), instruction[5]
    direction = numToDir[int(direction)]
    pos = addTuples(pos, scalarTuple(n, dirToVect[direction]))
    vertices.append(pos)
    boundary += n

# shoelace
area = 0
for i in range(len(vertices)-1):
    x, y= vertices[i]
    xx, yy = vertices[i+1]
    area += -(y+yy)*(x-xx) / 2

p2 = int(area + boundary/2 + 1)
print(p2)
