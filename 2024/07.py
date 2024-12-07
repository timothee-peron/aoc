import utils
from itertools import product
from functools import reduce

# utils.DEBUG = True
utils.printInfo()

data = utils.fileToLString(utils.inputFilePath()).strip().split('\n')
data = [l.split(': ') for l in data]
data = [(int(x), tuple(map(int, y.split(' ')))) for (x, y) in data]

def opZip(ns, os):
    assert(len(ns) == len (os) + 1)
    yield(ns[0])
    for i in range(len(os)):
        yield os[i]
        yield ns[i + 1]

assert(tuple(opZip([1,2,3], ('+', 'x'))) == (1,'+',2,'x',3))
 
def compute(l):
    it = iter(l)
    value = next(it)

    while True:
        operation = next(it, None)
        if operation is None:
            break
        v2 = next(it)
        if operation == '+':
            value += v2
        elif operation == 'x':
            value *= v2

    return value

assert(compute(tuple(opZip([1,2,3], ('+', 'x')))) == 9)

operators = "x+"
s = 0
for result, numbers in data:
    opss =  list(product(operators, repeat = len(numbers) - 1))
    for ops in opss:
        computation = list(opZip(numbers, ops))
        if(compute(computation) == result):
            s += result
            break
print(s)


def compute(l, target):
    it = iter(l)
    value = next(it)

    while True:
        if(value > target):
            break
        operation = next(it, None)
        if operation is None:
            break
        v2 = next(it)
        if operation == '+':
            value += v2
        elif operation == 'x':
            value *= v2
        elif operation == '|':
            value = int(str(value) + str(v2))

    return value

operators = "x+|"
s = 0
for result, numbers in data:
    opss =  list(product(operators, repeat = len(numbers) - 1))
    for ops in opss:
        computation = list(opZip(numbers, ops))
        if(compute(computation, result) == result):
            s += result
            break
print(s)
