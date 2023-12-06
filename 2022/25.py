import utils
from functools import reduce

# utils.DEBUG = True
utils.printInfo()

file = utils.fileToLines(utils.inputFilePath())

letterToNumber = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}

numberToLetter = {
    2: "2",
    1: "1",
    0: "0",
    -1: "-",
    -2: "=",
}

def snafuToDecimal(digits):
    rev = digits.copy()
    rev.reverse()
    value = 0
    operand = 1
    for digit in rev:
        value += letterToNumber[digit] * operand
        operand *= 5
    return value


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def decimalToSnafuBase(number):
    base5 = numberToBase(number, 5)

    def regularize(_digits):
        digits = _digits.copy()
        i = 0
        while i < len(digits):
            digit = digits[i]
            if digit > 2:
                digits[i] -= 5
                if i == 0:
                    digits.insert(0, 0)
                    i += 1
                digits[i - 1] += 1
            i += 1

        while digits[0] == 0:
            digits.pop(0)

        if not all(digit <= 2 for digit in digits):
            digits = regularize(digits)

        return digits

    return regularize(base5)


def decimalToSnafu(number):
    base5 = decimalToSnafuBase(number)
    return "".join([numberToLetter[d] for d in base5])


numbers = [snafuToDecimal(list(x)) for x in file]

total = sum(numbers)
print("PART1")
print(decimalToSnafu(total))
