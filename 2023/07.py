import utils
from functools import cmp_to_key
from collections import Counter

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLString(utils.inputFilePath()).split('\n')
data = [line.split(' ') for line in inputLines]
data = [(line[0], int(line[1])) for line in data]

order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

def htype(hand):
    c = Counter(hand)
    if 5 in c.values():
        return 6
    if 4 in c.values():
        return 5
    if 3 in c.values() and 2 in c.values():
        return 4
    if 3 in c.values():
        return 3
    if 2 in c.values():
        c2 = Counter(filter(lambda x: x == 2, c.values()))
        if 2 in c2.values():
            return 2
        else:
            return 1
    return 0

assert(htype('AAAAA') == 6)
assert(htype('AA8AA') == 5)
assert(htype('23332') == 4)
assert(htype('TTT98') == 3)
assert(htype('23432') == 2)
assert(htype('A23A4') == 1)
assert(htype('23456') == 0)

def cardCmp(a, b):
    ta, tb = htype(a[0]), htype(b[0])
    if ta < tb:
        return -1
    if ta > tb:
        return 1
    
    for ca, cb in zip(list(a[0]),list(b[0])):
        oa, ob = order.index(ca), order.index(cb)
        if(oa == ob):
            continue
        if oa > ob:
            return -1
        else:
            return 1
    raise(Error("2 same hands"))

orderedData = sorted(data, key=cmp_to_key(cardCmp), reverse=False)

score = 0
for index, s in enumerate(map(lambda x: x[1], orderedData)):
    score += (index+1) * s

print(score)

# part 2

order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def htype2(hand):
    handNoJ = list(filter(lambda c: c != 'J', hand))
    t1 = htype(handNoJ)
    c = Counter(hand)
    js = c['J']

    if js == 0:
        return t1
    
    if js == 5 or js == 4:
        return 6
    
    if js == 3:
        if t1 == 1:
            return 6
        return 5
    
    if js == 2:
        if t1 == 3:
            return 6
        if t1 == 1:
            return 5
        if t1 == 0:
            return 3
        raise Error("should not happen")

    if js == 1:
        if t1 == 5:
            return 6
        if t1 == 3:
            return 5
        if t1 == 2:
            return 4
        if t1 == 1:
            return 3
        if t1 == 0:
            return 1
        raise Error("should not happen")

    raise Error("should not happen")
    

assert(htype2('AAAAA') == 6)
assert(htype2('AA8AA') == 5)
assert(htype2('23332') == 4)
assert(htype2('TTT98') == 3)
assert(htype2('23432') == 2)
assert(htype2('A23A4') == 1)
assert(htype2('23456') == 0)
assert(htype2('AAAJJ') == 6)
assert(htype2('AAJJJ') == 6)
assert(htype2('AKJJJ') == 5)
assert(htype2('AAKJJ') == 5)
assert(htype2('AQKJJ') == 3)
assert(htype2('AJ8AA') == 5)
assert(htype2('23J32') == 4)
assert(htype2('TJT98') == 3)
assert(htype2('23432') == 2)
assert(htype2('J23A4') == 1)
assert(htype2('23456') == 0)

def cardCmp(a, b):
    ta, tb = htype2(a[0]), htype2(b[0])
    if ta < tb:
        return -1
    if ta > tb:
        return 1
    
    for ca, cb in zip(list(a[0]),list(b[0])):
        oa, ob = order.index(ca), order.index(cb)
        if(oa == ob):
            continue
        if oa > ob:
            return -1
        else:
            return 1
    raise(Error("2 same hands"))

orderedData = sorted(data, key=cmp_to_key(cardCmp), reverse=False)

score = 0
for index, s in enumerate(map(lambda x: x[1], orderedData)):
    score += (index+1) * s

print(score)