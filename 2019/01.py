import utils

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())

def fuel(m):
    return m // 3 - 2

assert(33583 == fuel(100756))

print(sum(map(fuel, utils.linesToNumbers(inputLines))))

def fuel2(m):
    m2 = m // 3 - 2
    if m2 <= 0:
        return 0
    return m2 + fuel2(m2)

assert(50346 == fuel2(100756))

print(sum(map(fuel2, utils.linesToNumbers(inputLines))))
