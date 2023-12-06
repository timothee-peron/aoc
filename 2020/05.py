import utils

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.linesToItems(utils.fileToLines(utils.inputFilePath()), list)

def getRow(seat):
    l = seat[0:7][::-1]
    r = 0
    b = 1
    for s in l:
        r += b * ( 1 if s =='B' else 0)
        b *= 2
    return r

def getCol(seat):
    l = seat[-3:][::-1]
    r = 0
    b = 1
    for s in l:
        r += b * ( 1 if s =='R' else 0)
        b *= 2
    return r

def getId(seat):
    return getRow(seat) * 8 + getCol(seat)

assert(getRow(list('FBFBBFFRLR')) == 44)
assert(getCol(list('FBFBBFFRLR')) == 5)
assert(getId(list('FBFBBFFRLR')) == 357)
assert(getId(list('BFFFBBFRRR')) == 567)
assert(getId(list('FFFBBBFRRR')) == 119)
assert(getId(list('BBFFBBFRLL')) == 820)

allIds = list(map(getId, inputLines))
print(max(allIds))

allIds.sort()
lastId = None
for x in allIds:
    if lastId is None:
        lastId = x
        continue
    if x != lastId + 1:
        print(lastId + 1)
        break
    lastId = x
