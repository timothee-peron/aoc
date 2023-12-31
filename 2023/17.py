import utils
from collections import defaultdict
from math import inf

# utils.DEBUG = True
utils.printInfo()

fp = utils.inputFilePath()
data = list(map(list, utils.fileToLString(fp).strip().split('\n')))
data = [[int(y) for y in x] for x in data]

H, W = len(data), len(data[0])

NORTH, WEST, SOUTH, EAST = 0, 1, 2, 3

def printPath(matrix, path):
    p = set(path)
    for y, row in enumerate(matrix):
        for x, h in enumerate(row):
            if (x, y) in p:
                print('·', end='')
            else:
                print(str(h), end='')
        print('')

# Dijkstra with 2D array matrix, nodes are 4D (x, y, direction, countstraight)
# source is 4D, end is 2D
def dijkstra(matrix, source, end):
    distances = defaultdict(lambda: inf)
    distances[source] = 0
    predecessors = defaultdict(lambda: None)

    q = [source]
    q = set(q)

    while q:

        # print(len(q))
        # find min distance in q:
        _min = None

        for node in q:
            if _min is None or distances[node] < distances[_min]:
                _min = node

        if _min is None:
            break

        x, y, d, s = _min
        q.remove(_min)

        # check if found the end
        if (x, y) == end:
            break

        neighbors = []
        neighbors.append((x, y-1, NORTH, s + 1 if d == NORTH else 1))
        neighbors.append((x, y+1, SOUTH, s + 1 if d == SOUTH else 1))
        neighbors.append((x+1, y, EAST, s + 1 if d == EAST else 1))
        neighbors.append((x-1, y, WEST, s + 1 if d == WEST else 1))

        for neighbor in neighbors:
            x, y, d2, s = neighbor
            if not (0 <= x < W and 0 <= y < H):
                # not in grid
                continue
            if s > 3:
                # more than 3 in straight line
                continue
            if not(d2 == d or d2 == (d + 1) % 4 or d2 == (d - 1) % 4):
                # only 90 deg turn or straight
                continue
            else:
                pass
            
            # total heat loss
            heatLoss = matrix[y][x] + distances[_min]
            if heatLoss < distances[neighbor]:
                distances[neighbor] = heatLoss
                predecessors[neighbor] = _min

                q.add(neighbor) # we need to visit neighbor's neighors
    
    return (predecessors, distances)




end = (W -1, H -1)
predecessors, distances = dijkstra(data, (0, 0, EAST, 0), end)

# find node matching end position with minimal distance
endNode = None
endDist = inf
for node, d in distances.items():
    x, y, _, s = node
    if (x, y) == end and s <= 3:
        if d < endDist:
            endNode = node
            endDist = d

# part 1 (quite slow)
print(distances[endNode])

if utils.DEBUG:
    # show path for check
    path = [endNode]
    while not (path[-1][0] == 0 and path[-1][1] == 0):
        path.append(predecessors[path[-1]])

    path.reverse()

    path = [(x, y) for x, y, _, _ in path]
    printPath(data, path)
