import utils
from sortedcontainers import SortedKeyList
from collections import defaultdict, deque

utils.DEBUG = False
utils.printInfo()

data = [list(line) for line in utils.fileToLString(utils.inputFilePath()).strip().split('\n')]

EAST,SOUTH,WEST,NORTH=0,1,2,3

def dirToVector(d):
    if d == EAST:
        return (1,0)
    if d == SOUTH:
        return (0,1)
    if d == WEST:
        return (-1,0)
    if d == NORTH:
        return (0,-1)

start, end = None, None
walls, empty = set(), set()

for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c == 'S':
            start = (x,y,EAST)
        elif c == 'E':
            end = (x,y)
        
        if c == '#':
            walls.add((x,y))
        else:
            empty.add((x,y))


def getAdjacent(node):
    x,y,d = node
    u, v = dirToVector(d)
    adj = []

    if (x+u,y+v) in empty:
        adj.append(((x+u, y+v, d), 1))
    
    
    adj.append(((x, y, (d + 1) % 4),   1000))
    adj.append(((x, y, (d - 1) % 4),   1000))

    return adj

q = SortedKeyList([(start, 0)], key=lambda x: x[1])
distances = {start: 0}
minDistance = None
previous = defaultdict(set)
while len(q) > 0:
    u, d = q.pop(0)
    if u in distances and d > distances[u]:
        continue

    if u[0] == end[0] and u[1] == end[1]:
        minDistance = distances[u]

    for v, dist in getAdjacent(u):
        dist = d + dist
        if v in distances and dist > distances[v]:
            continue

        if minDistance != None and minDistance < dist:
            continue

        previous[v].add(u)
        distances[v] = dist
        q.add((v, dist))

print(minDistance)

ends = []
for i in range(4):
    if (end[0], end[1], i) in distances and distances[(end[0], end[1], i)] == minDistance:
        ends.append((end[0], end[1], i))


q = deque(ends)
visited = set(ends)
while len(q) > 0:
    v = q.pop()
    visited.add(v)
    for p in previous[v]:
        q.appendleft(p)
visited = set((x,y) for x,y,_ in visited)
print(len(visited))
