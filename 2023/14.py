import utils
import copy

# utils.DEBUG = True
utils.printInfo()

data = utils.fileToLString(utils.inputFilePath()).strip().split('\n')
data = [list(x) for x in data]

def prnt(arr):
    print("\n".join(["".join(x) for x in arr]))

# part 1
def moveRocksN(arr):
    _arr = copy.deepcopy(arr)
    for x in range(len(_arr[0])):
        y = 0
        while y < len(_arr):
            if _arr[y][x] == 'O':
                if y > 0 and _arr[y - 1][x] == '.':
                    _arr[y][x] = '.'
                    y += -1
                    _arr[y][x] = 'O'
                else:
                     y += 1
            else:
                y += 1
    return _arr

def computeLoadN(arr):
    load = 0
    H = len(arr)
    for y, row in enumerate(arr):
        for x in row:
            if x == 'O':
                load += H - y
    return load


northed = moveRocksN(data)
print(computeLoadN(northed))

# part2:
def moveRocksS(arr):
    return list(reversed(moveRocksN(list(reversed(arr)))))

def transpose(arr):
    t = [list(x) for x in zip(*arr)]
    return t

def moveRocksW(arr):
    return transpose(moveRocksN(transpose(arr)))

def moveRocksE(arr):
    return transpose(moveRocksS(transpose(arr)))

def cycle(arr):
    _arr = moveRocksN(arr)
    _arr = moveRocksW(_arr)
    _arr = moveRocksS(_arr)
    _arr = moveRocksE(_arr)
    return _arr

def hashArr(arr):
    return "".join(["".join(x) for x in arr])

statesArr = [hashArr(data)]
statesSet = {hashArr(data)}
_data = data
i = 0
while True:
    _data = cycle(_data)
    i += 1
    h = hashArr(_data)
    if h in statesSet:
        break
    statesArr.append(h)
    statesSet.add(h)

j = i
i = statesArr.index(h)

loop = j - i
remain = (1_000_000_000 - i) % (j - i)

for _ in range(remain):
    _data = cycle(_data)

print(computeLoadN(_data))
