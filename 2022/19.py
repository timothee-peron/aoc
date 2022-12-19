from queue import Queue
from itertools import permutations
import math

import utils
import numpy as np

utils.DEBUG = True
utils.DEBUG = False
utils.printInfo()

part1 = True
part2 = True

inputLines = utils.fileToLines(utils.inputFilePath())
# wholeFile = utils.fileToLString(utils.inputFilePath())

# Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay.
# Each geode robot costs 2 ore and 7 obsidian.

digits = [utils.digitsInString(line) for line in inputLines]
# bp number, ore robot cost (ore), clay r cost (ore), obs cost (ore, clay), geode (ore, obs)

endStates = []
for id, orerOreCost, clarOreCost, obsrOreCost, obsrClayCost, georOreCost, georObsCost in digits:
    if not part1:
        break
    print(f"PART1 ID {id} starts...")
    # state = {
    #     "orer": 1,
    #     "clar": 0,
    #     "obsr": 0,
    #     "geor": 0,
    #     "ore": 0,
    #     "cla": 0,
    #     "obs": 0,
    #     "geo": 0,
    # }
    state = (1, 0, 0, 0, 0, 0, 0, 0)
    states = set()
    states.add(state)

    factor = 12
    oreCheck = factor * max(georOreCost, obsrOreCost, clarOreCost, orerOreCost)
    obsCheck = factor * georObsCost
    claCheck = factor * obsrClayCost

    for i in range(24):
        print(f"PART1 ID {id} step {i}")
        nextStates = set()
        maxgeo = 0
        for state in states:
            orer, clar, obsr, geor, ore, cla, obs, geo = state
            ore2 = ore + orer
            cla2 = cla + clar
            obs2 = obs + obsr
            geo2 = geo + geor
            if geo2 > maxgeo:
                maxgeo = geo2

            if ore > oreCheck or obs > obsCheck or cla > claCheck:
                continue
            if ore >= georOreCost and obs >= georObsCost:
                nextStates.add((orer, clar, obsr, geor + 1, ore2 - georOreCost, cla2, obs2 - georObsCost, geo2))
            else:
                if ore >= obsrOreCost and cla >= obsrClayCost:
                    nextStates.add((orer, clar, obsr + 1, geor, ore2 - obsrOreCost, cla2 - obsrClayCost, obs2, geo2))
                else:
                    if ore >= clarOreCost:
                        nextStates.add((orer, clar + 1, obsr, geor, ore2 - clarOreCost, cla2, obs2, geo2))
                    if ore >= orerOreCost:
                        nextStates.add((orer + 1, clar, obsr, geor, ore2 - orerOreCost, cla2, obs2, geo2))
                    if ore < 5:
                        nextStates.add((orer, clar, obsr, geor, ore2, cla2, obs2, geo2))

        states = nextStates
        # discard geos
        toDiscard = set()
        for state in states:
            orer, clar, obsr, geor, ore, cla, obs, geo = state
            if geo < maxgeo:
                toDiscard.add(state)

        for state in toDiscard:
            states.discard(state)

    maxgeo = 0
    maxState = None
    for state in states:
        if state[7] > maxgeo:
            maxgeo = state[7]
            maxState = state
    endStates.append((id, maxgeo))
    # endStates.append((id, state))

    print(f"PART1 ID {id} success!")

print("Part1")
s = 0
for id, geos in endStates:
    s += id * geos
print(s)

# part 2
endStates = []
for id, orerOreCost, clarOreCost, obsrOreCost, obsrClayCost, georOreCost, georObsCost in digits[0:3]:
    if not part2:
        break
    print(f"PART2 ID {id} starts...")
    # state = {
    #     "orer": 1,
    #     "clar": 0,
    #     "obsr": 0,
    #     "geor": 0,
    #     "ore": 0,
    #     "cla": 0,
    #     "obs": 0,
    #     "geo": 0,
    # }
    state = (1, 0, 0, 0, 0, 0, 0, 0)
    states = set()
    states.add(state)

    factor = 12
    oreCheck = factor * max(georOreCost, obsrOreCost, clarOreCost, orerOreCost)
    obsCheck = factor * georObsCost
    claCheck = factor * obsrClayCost

    for i in range(32):
        print(f"PART2 ID {id} step {i}")
        nextStates = set()
        maxgeo = 0
        for state in states:
            orer, clar, obsr, geor, ore, cla, obs, geo = state
            ore2 = ore + orer
            cla2 = cla + clar
            obs2 = obs + obsr
            geo2 = geo + geor
            if geo2 > maxgeo:
                maxgeo = geo2

            if ore > oreCheck or obs > obsCheck or cla > claCheck:
                continue
            if ore >= georOreCost and obs >= georObsCost:
                nextStates.add((orer, clar, obsr, geor + 1, ore2 - georOreCost, cla2, obs2 - georObsCost, geo2))
            else:
                if ore >= obsrOreCost and cla >= obsrClayCost:
                    nextStates.add((orer, clar, obsr + 1, geor, ore2 - obsrOreCost, cla2 - obsrClayCost, obs2, geo2))
                else:
                    if ore >= clarOreCost:
                        nextStates.add((orer, clar + 1, obsr, geor, ore2 - clarOreCost, cla2, obs2, geo2))
                    if ore >= orerOreCost:
                        nextStates.add((orer + 1, clar, obsr, geor, ore2 - orerOreCost, cla2, obs2, geo2))
                    if ore < 5:
                        nextStates.add((orer, clar, obsr, geor, ore2, cla2, obs2, geo2))

        states = nextStates
        # discard geos
        toDiscard = set()
        for state in states:
            orer, clar, obsr, geor, ore, cla, obs, geo = state
            if geo < maxgeo:
                toDiscard.add(state)

        for state in toDiscard:
            states.discard(state)

    maxgeo = 0
    maxState = None
    for state in states:
        if state[7] > maxgeo:
            maxgeo = state[7]
            maxState = state
    endStates.append(maxgeo)
    # endStates.append((id, state))

    print(f"PART2 ID {id} success!")

print("PART1")
print(s)
print("PART2")
s2 = 1
for i, geos in enumerate(endStates):
    print(f"max geos for i was {geos}")
    s2 *= geos
print(s2)
