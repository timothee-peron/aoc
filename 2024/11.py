import utils

# utils.DEBUG = True
utils.printInfo()

data = list(map(int, utils.fileToLString(utils.inputFilePath()).split(' ')))

def oneStep(stone):
    if stone == 0:
        return [1]
    sstone = str(stone)
    if len(sstone) % 2 == 0:
        s1 = sstone[0:len(sstone)//2]
        s2 = sstone[len(sstone)//2:]
        return [int(s1), int(s2)]
    return [stone * 2024]

assert(oneStep(0)[0] == 1)
assert(oneStep(4512)[0] == 45)
assert(oneStep(4512)[1] == 12)
assert(oneStep(45123)[0] == 45123*2024)

def blink(stones):
    res = []
    for s in stones:
        for ss in oneStep(s):
            res.append(ss)
    return res

for i in range(25):
    data = blink(data)

print(len(data))

data = tuple(map(int, utils.fileToLString(utils.inputFilePath()).split(' ')))

memo = {}
def solveOne(stone, n):
    if (stone, n) in memo:
        return memo[(stone,n)]
    if n == 0:
        r = 1
    else:
        r = 0
        sstone = str(stone)
        if stone == 0:
            r = solveOne(1, n - 1)
        elif len(sstone) % 2 == 0:
            s1 = sstone[0:len(sstone)//2]
            s2 = sstone[len(sstone)//2:]
            r = solveOne(int(s1), n - 1) + solveOne(int(s2), n - 1)
        else:
            r = solveOne(stone * 2024, n - 1)

    memo[(stone, n)] = r
    return r

print(sum(solveOne(s, 75) for s in data))