import utils
import itertools

# utils.DEBUG = True
utils.printInfo()

data = utils.fileToLString(utils.inputFilePath()).split('\n')

H = len(data)
W = len(data[0])

emptyCols = []
emptyRows = []

for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c == '#':
            break
    else:
        emptyRows.append(y)

for x in range(W):
    for y in range(H):
        c = data[y][x]
        if c == '#':
            break
    else:
        emptyCols.append(x)

emptyCols = set(emptyCols) # x
emptyRows = set(emptyRows) # y

y = 0
gPos = []
for _y, line in enumerate(data):
    x = 0
    for _x, c in enumerate(line):
        if c == '#':
            gPos.append((len(gPos) + 1, (x, y)))
            # print(gPos[-1])
        if _x in emptyCols:
            x += 2
        else:
            x += 1

    if _y in emptyRows:
        y += 2
    else:
        y += 1

# print(gPos)
gpairs = list(itertools.combinations(gPos, 2))

distances = []
for g1, g2 in gpairs:
    i1, (x1, y1) = g1
    i2, (x2, y2) = g2
    d = abs(y2 - y1) + abs(x2 - x1)
    # print(g1, g2, d)
    distances.append(d)

print(sum(distances))



# Part 2

emptyCols = []
emptyRows = []

for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c == '#':
            break
    else:
        emptyRows.append(y)

for x in range(W):
    for y in range(H):
        c = data[y][x]
        if c == '#':
            break
    else:
        emptyCols.append(x)

emptyCols = set(emptyCols) # x
emptyRows = set(emptyRows) # y

y = 0
gPos = []
for _y, line in enumerate(data):
    x = 0
    for _x, c in enumerate(line):
        if c == '#':
            gPos.append((len(gPos) + 1, (x, y)))
            # print(gPos[-1])
        if _x in emptyCols:
            x += 1000000
        else:
            x += 1

    if _y in emptyRows:
        y += 1000000
    else:
        y += 1

# print(gPos)
gpairs = list(itertools.combinations(gPos, 2))

distances = []
for g1, g2 in gpairs:
    i1, (x1, y1) = g1
    i2, (x2, y2) = g2
    d = abs(y2 - y1) + abs(x2 - x1)
    # print(g1, g2, d)
    distances.append(d)

print(sum(distances))

