import utils
import numpy as np

# from sortedcontainers import *

utils.DEBUG = True
utils.DEBUG = False
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
wholeFile = utils.fileToLString(utils.inputFilePath())

cycles = {
    "add": 2,
    "noop": 1,
}

instructions = [line.split(' ') for line in inputLines]

register = [1]

for instruction in instructions:
    value = register[-1]
    if instruction[0] == "noop":
        register.append(value)
        continue

    register.append(value)
    add = int(instruction[1])
    value = register[-1] + add
    register.append(value)

# print(register)
interesting = register[20::40]
interesting = range(20, 221, 40)

part11 = [register[i - 1] for i in interesting]
part1 = [i * register[i - 1] for i in interesting]
print("PART1")
print(sum(part1))

print("PART2")
screen = np.zeros((6, 40))


def printScreen(_s):
    print("")
    for line in _s:
        display = "".join(['##' if i == 1 else ".." for i in line])
        print(display)
    print("")


i = 0
for y in range(6):
    for x in range(40):
        pos = register[i]
        if x in [pos, pos + 1, pos - 1]:
            screen[y][x] = 1
        i += 1

printScreen(screen)
