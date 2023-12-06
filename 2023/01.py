import utils

from sortedcontainers import SortedDict

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())

nums = [list(map(int, filter(lambda v: v.isdigit(), list(x)))) for x  in inputLines]
calVals = []
for val in nums:
    calVals.append(val[0] * 10 + val[-1])
print(sum(calVals))

searches = {
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9
}

calVals = []
for line in inputLines:
    numbers = SortedDict()

    for k, v in searches.items():
        f = line.find(k)
        l = line.rfind(k)

        if f is not -1:
            numbers[f] = v
            numbers[l] = v
    keys = numbers.keys()
    calVals.append(numbers[keys[0]] * 10 + numbers[keys[ - 1]])
print(sum(calVals))
