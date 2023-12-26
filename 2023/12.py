import utils
import itertools
from collections import Counter
from functools import cache

# utils.DEBUG = True
utils.printInfo()

data = list(map(lambda x: x.split(' '), filter(lambda x: x != "", utils.fileToLString(utils.inputFilePath()).split('\n'))))
for z in data:
    x, y = z
    x = tuple(x)
    y = tuple(map(int, y.split(',')))
    z[0] = x
    z[1] = y

# part 1 (bruteforce)

@cache
def replaceInStrArray(str1, replArr):
    str2 = []
    i = 0
    for c in str1:
        if c == '?':
            str2.append(replArr[i])
            i += 1
        else:
            str2.append(c)
    return tuple(str2)

# get damaged groups
@cache
def strDmg(_str):
    _dmg = []
    status = None
    for c in _str:
        if status == None:
            status = c
            if status == '#':
                _dmg.append(1)
            continue

        newStatus = c
        if newStatus == '#':
            if newStatus == status:
                _dmg[-1] += 1
            else:
                _dmg.append(1)

        status = newStatus
    return tuple(_dmg)

i = 0
valid = 0
for chars, damaged in data:
    cnt = Counter(chars)
    repl = itertools.product(['.', '#'], repeat=cnt['?'])
    
    # print(chars)
    for _repl in repl:
        candidate = replaceInStrArray(chars, _repl)
        if strDmg(candidate) == damaged:
            valid += 1
    # repl = list(repl)
    # print(repl)

    i+=1
    print(i)

print(valid)
if not utils.DEBUG:
    assert valid == 7379

