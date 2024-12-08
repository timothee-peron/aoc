import utils
from itertools import permutations
from collections import defaultdict

# utils.DEBUG = True
utils.printInfo()

data = utils.fileToLString(utils.inputFilePath()).strip().split('\n')
data = [list(l) for l in data]

H = len(data)
L = len(data[0])

allLetters = defaultdict(set)
for y, l in enumerate(data):
    for x, c in enumerate(l):
        if c is not '.':
            allLetters[c].add((x, y))

antinodepos = set()
for key, poss in allLetters.items():
    for a, b in permutations(poss, 2):
        xa, ya = a
        xb, yb = b
        u = xb - xa
        v = yb - ya
        if 0 <= xa -u < L and 0 <= ya -v < H:
            antinodepos.add((xa -u, ya -v))
        if 0 <= xb +u < L and 0 <= yb +v < H:
            antinodepos.add((xb +u, yb +v))

print(len(antinodepos))

antinodepos = set()
for key, poss in allLetters.items():
    for a, b in permutations(poss, 2):
        xa, ya = a
        xb, yb = b
        u = xb - xa
        v = yb - ya
        antinodepos.add((xa, ya))
        antinodepos.add((xb, yb))
        while 0 <= xa -u < L and 0 <= ya -v < H:
            xa -= u
            ya -= v
            antinodepos.add((xa, ya))
        
        while 0 <= xb +u < L and 0 <= yb +v  < H:
            xb += u
            yb += v
            antinodepos.add((xb, yb))

print(len(antinodepos))
