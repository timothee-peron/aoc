# pylint: disable=cell-var-from-loop broad-exception-raised unnecessary-negation

import utils

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLString(utils.inputFilePath()).split('\n')
times = inputLines[0].split(' ')[1:]
times = list(filter(lambda x: x != '', times))
times = list(map(int, times))
distance = inputLines[1].split(' ')[1:]
distance = list(filter(lambda x: x != '', distance))
distance = list(map(int, distance))

races = list(zip(times, distance))


def product(arr):
    result = 1
    for v in arr:
        result *= v
    return result

wins = []
for time, distance in races:
    hold = list(range(time + 1))
    d = list(map(lambda t: t * (time - t), hold))
    d = list(filter(lambda x: x > distance, d))
    wins.append(len(d))
print(product(wins))

# part 2
times = inputLines[0].split(' ')[1:]
times = list(filter(lambda x: x != '', times))
time=int("".join(times))
distance = inputLines[1].split(' ')[1:]
distance = list(filter(lambda x: x != '', distance))
distance=int("".join(distance))

# find one win
t = time / 2
if not t * (time - t) > distance:
    raise(Exception('ouch'))


# find min wining
a = 0
b = time // 2

while b != a + 1:
    mid = (a + b) // 2
    t = mid
    wins = t * (time - t) > distance
    if wins:
        b= mid
    else:
        a = mid

firstWin = b


# find last wining
a = time // 2
b = time

while b != a + 1:
    mid = (a + b) // 2
    t = mid
    wins = t * (time - t) > distance
    if wins:
        a= mid
    else:
        b = mid
lastWin = a

print(lastWin - firstWin +1)
