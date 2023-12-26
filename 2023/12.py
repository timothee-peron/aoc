import utils
import itertools
from functools import cache

# utils.DEBUG = True
utils.printInfo()

data = utils.fileToLines(utils.inputFilePath())

@cache
def dynamicPrg(chars, states):
    total = 0

    if len(chars) == 0:
        if len(states) == 0:
            return 1
        return 0

    if len(states) == 0:
        if "#" in chars:
            return 0
        return 1

    if len(chars) < sum(states) + len(states) - 1:
        return 0

    if chars[0] in ".?":
        total += dynamicPrg(chars[1:], states)

    n = states[0]
    if (
        chars[0] in "#?"
        and "." not in chars[:n]
        and (len(chars) == n or chars[n] in ".?")
    ):
        total += dynamicPrg(chars[n + 1 :], states[1:])

    return total


def solve(lines, fold):
    count = 0
    for line in lines:
        chars, states = line.split(" ")
        chars = "?".join([chars] * fold)
        states = tuple(int(n) for n in states.split(",")) * fold
        count += dynamicPrg(chars, states)
    return count


print(solve(data, 1))
print(solve(data, 5))
