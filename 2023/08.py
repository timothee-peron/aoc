import utils
import itertools
from math import lcm

# utils.DEBUG = True
utils.printInfo()

data = utils.fileToLString(utils.inputFilePath()).split('\n\n')
instructions = list(data[0])

lines = data[1].split('\n')
nodes = {}
for node in lines:
    v = node[0:3]
    l = node[7:10]
    r = node[12:15]
    nodes[v] = (l, r)

#part 1
start, end = 'AAA', 'ZZZ'

pos = start
arrived = False
cnt = 0
while not arrived:
    for l in instructions:
        if l == 'L':
            pos = nodes[pos][0]
        else:
            pos = nodes[pos][1]
        cnt += 1
        if pos == end:
            arrived = True
            break

print(cnt)

# part 2
starts, ends = [], []
for node in nodes.keys():
    if node[2] == 'A':
        starts.append(node)
    if node[2] == 'Z':
        ends.append(node)

poss = [s for s in starts]

toEndCnts = []
for pos in poss:
    done = False
    cnt = 0
    thisEnds = {}
    while not done:
        for l in instructions:
            if l == 'L':
                pos = nodes[pos][0]
            else:
                pos = nodes[pos][1]
            
            cnt += 1
            if pos in ends:
                if pos in thisEnds.keys():
                    done = True
                    break
                else:
                    thisEnds[pos] = cnt
    toEndCnts.append(list(thisEnds.values()))

comb = list(itertools.product(*toEndCnts))
lcms = [lcm(*x) for x in comb]
print(min(lcms))