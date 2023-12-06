import utils

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
table = utils.linesToChars(inputLines)

def startNumber(nl, c, _x, _y):
    nl.append({"chars": [c], "coords": {(_x, _y)}})


def appendNumber(nl, c, _x, _y):
    nl[-1]['chars'].append(c)
    nl[-1]['coords'].add((_x, _y))

def getValueAt(_map, _x, _y):
    if (_x >= 0 and _x < len(_map[0]) and _y >= 0 and _y < len(_map)):
        value = _map[_y][_x]
        return value
    return None

def getAdjacentValues(_map, _x, _y):
    results = []
    points = [(_x, _y + 1), (_x, _y - 1), (_x + 1, _y), (_x - 1, _y),
    (_x +1, _y + 1), (_x -1, _y - 1), (_x + 1, _y -1 ), (_x - 1, _y +1)]
    for point in points:
        value = getValueAt(_map, point[0], point[1])
        if value is not None:
            results.append(value)
    return results

def getAdjacentCoords(_x, _y):
    return [(_x, _y + 1), (_x, _y - 1), (_x + 1, _y), (_x - 1, _y),
    (_x +1, _y + 1), (_x -1, _y - 1), (_x + 1, _y -1 ), (_x - 1, _y +1)]

def getManyAdjacentValues(_map, coords):
    results = set()
    for _x, _y in coords:
        results = results.union(set(getAdjacentValues(_map, _x, _y)))
    return results

def getManyAdjacentCoords(coords):
    results = set()
    for _x, _y in coords:
        results = results.union(set(getAdjacentCoords(_x, _y)))
    return results

digits = frozenset({"0","1","2","3","4","5","6","7","8","9"})
def charIsNum(_c):
    return _c in digits

def numToValue(n):
    chars = n['chars']
    chars = reversed(chars)
    result = 0
    p = 1
    for c in chars:
        result += int(c) * p
        p *= 10
    return result

assert(numToValue({'chars': ['6', '3', '3'], 'coords': {(8, 2), (6, 2), (7, 2)}}) == 633)

def isValidNumberPart1(_num):
    coords = _num['coords']
    adj = getManyAdjacentValues(table, coords)
    adj = filter(lambda c: c != '.', adj)
    adj = filter(lambda c: not charIsNum(c), adj)
    return len(list(adj)) > 0

def product(arr):
    result = 1
    for v in arr:
        result *= v
    return result

numbers = []
for y, row in enumerate(table):
    isInNumber = False
    for x, char in enumerate(row):
        if charIsNum(char):
            if isInNumber:
                appendNumber(numbers, char, x, y)
            else:
                isInNumber = True
                startNumber(numbers, char, x, y)
        else:
            isInNumber = False

validNumbers = list(filter(isValidNumberPart1, numbers))
print(sum(list(map(numToValue, validNumbers))))

potentialGears = []
for y, row in enumerate(table):
    for x, char in enumerate(row):
        if char == '*':
            potentialGears.append((x,y))

for num in numbers:
    num['adj'] = getManyAdjacentCoords(num['coords'])

okGears = []
for pos in potentialGears:
    cntNum = 0
    nums = []
    for num in numbers:
        if pos in num['adj']:
            cntNum += 1
            nums.append(numToValue(num))
            continue
    
    if cntNum == 2:
        okGears.append(product(nums))
print(sum(okGears))
