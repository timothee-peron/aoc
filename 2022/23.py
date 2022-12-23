import utils
from collections import Counter

utils.DEBUG = True
utils.DEBUG = False
utils.printInfo()

file = utils.fileToLines(utils.inputFilePath())


def prnt(topLeft, bottomRight, elves):
    print('#################')
    for y in range(topLeft[1], bottomRight[1] + 1):
        for x in range(topLeft[0], bottomRight[0] + 1):
            print('#' if (x, y) in elves else '.', end='')
        print('')
    print('')


def adjacent(coords):
    x, y = coords
    return [(x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
            (x + 1, y - 1),
            (x - 1, y - 1),
            (x - 1, y + 1),
            (x + 1, y + 1)]


def computeRect(elves):
    topLeft = None
    bottomRight = None

    for x, y in elves:
        if topLeft is None:
            topLeft = (x, y)
            bottomRight = (x, y)
            continue

        if x < topLeft[0]:
            topLeft = (x, topLeft[1])

        if y < topLeft[1]:
            topLeft = (topLeft[0], y)

        if x > bottomRight[0]:
            bottomRight = (x, bottomRight[1])

        if y > bottomRight[1]:
            bottomRight = (bottomRight[0], y)
    return (topLeft, bottomRight)


def positionConsidered(x, y, roundNumber):
    rn = roundNumber % 4
    results = []
    results.append( ( (x, y - 1), ( (x - 1, y - 1), (x, y - 1), (x + 1, y - 1) ) ) )
    results.append( ( (x, y + 1), ( (x - 1, y + 1), (x, y + 1), (x + 1, y + 1) ) ) )
    results.append( ( (x - 1, y), ( (x - 1, y + 1), (x - 1, y), (x - 1, y - 1) ) ) )
    results.append( ( (x + 1, y), ( (x + 1, y + 1), (x + 1, y), (x + 1, y - 1) ) ) )
    for _ in range(rn):
        last = results.pop(0)
        results.append(last)
    return results


def part1():
    elves = set()
    for y, row in enumerate(file):
        for x, char in enumerate(row):
            if char == '#':
                elves.add((x, y))
    total = len(elves)
    for roundNumber in range(10):
        # if utils.DEBUG:
        #     print(roundNumber)
        #     tl, br = computeRect(elves)
        #     prnt(tl, br, elves)

        proposedPositions = {}

        # part 1:
        for x, y in elves:
            adj = adjacent((x, y))
            alone = True
            for elf in adj:
                if elf in elves:
                    alone = False
                    break

            if alone:
                continue

            stackDecisions = positionConsidered(x, y, roundNumber)
            for decision in stackDecisions:
                goal, checks = decision
                emptyDecision = True
                for check in checks:
                    if check in elves:
                        emptyDecision = False
                        continue

                if not emptyDecision:
                    continue

                proposedPositions[(x, y)] = goal
                break

        # part 2
        destinations = Counter(proposedPositions.values())

        for elf, destination in proposedPositions.items():
            if destinations[destination] != 1:
                continue

            elves.remove(elf)
            elves.add(destination)

        assert total == len(elves)

    topLeft, bottomRight = computeRect(elves)

    rectangleSize = (bottomRight[0] - topLeft[0] + 1, bottomRight[1] - topLeft[1] + 1)
    cnteleves = len(elves)
    area = rectangleSize[0] * rectangleSize[1]
    empty = area - cnteleves
    return empty

print('PART1')
empty = part1()
print(empty)


def part2():
    elves = set()
    for y, row in enumerate(file):
        for x, char in enumerate(row):
            if char == '#':
                elves.add((x, y))
    total = len(elves)

    roundNumber = 0
    while True:
        # if utils.DEBUG:
        #     print(roundNumber)
        #     tl, br = computeRect(elves)
        #     prnt(tl, br, elves)

        proposedPositions = {}

        # part 1:
        for x, y in elves:
            adj = adjacent((x, y))
            alone = True
            for elf in adj:
                if elf in elves:
                    alone = False
                    break

            if alone:
                continue

            stackDecisions = positionConsidered(x, y, roundNumber)
            for decision in stackDecisions:
                goal, checks = decision
                emptyDecision = True
                for check in checks:
                    if check in elves:
                        emptyDecision = False
                        continue

                if not emptyDecision:
                    continue

                proposedPositions[(x, y)] = goal
                break

        roundNumber += 1
        if len(proposedPositions) == 0:
            break

        # part 2
        destinations = Counter(proposedPositions.values())

        for elf, destination in proposedPositions.items():
            if destinations[destination] != 1:
                continue

            elves.remove(elf)
            elves.add(destination)

        assert total == len(elves)

    return roundNumber

print('PART2')
roundNumber = part2()
print(roundNumber)
