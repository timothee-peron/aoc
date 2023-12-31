import utils
from collections import defaultdict
from math import inf
from pqdict import pqdict

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
                print(' ', end='')
            else:
                print(str(h), end='')
        print('')

# Dijkstra with 2D array matrix, nodes are 3D (x, y, direction)
# start, end are 2D
def dijkstra(matrix, source, end, MIN_JUMP, MAX_JUMP):
    _sources = [(source[0], source[1], SOUTH), (source[0], source[1], EAST)]
    distances = defaultdict(lambda: inf)
    for _source in _sources:
        distances[_source] = 0
    predecessors = defaultdict(lambda: None)

    q = pqdict.minpq()
    
    for _source in _sources:
        q[_source] = 0

    while q:
        # find min distance in q:
        _min, _ = q.popitem()
        x, y, d = _min

        neighbors = []
        for i in range(MIN_JUMP, MAX_JUMP + 1):
            neighbors.append((x, y-i, NORTH))
            neighbors.append((x, y+i, SOUTH))
            neighbors.append((x+i, y, EAST))
            neighbors.append((x-i, y, WEST))

        for neighbor in neighbors:
            x2, y2, d2 = neighbor
            if not (0 <= x2 < W and 0 <= y2 < H):
                # not in grid
                continue
            if (d - d2) % 2 == 0:
                continue
            
            # total heat loss
            heatLoss = distances[_min]

            if x == x2:
                for _y in range(min(y, y2), max(y, y2) + 1):
                    heatLoss += matrix[_y][x]
            else:
                for _x in range(min(x, x2), max(x, x2) + 1):
                    heatLoss += matrix[y][_x]
            heatLoss -= matrix[y][x] # because counted twice

            if heatLoss < distances[neighbor]:
                distances[neighbor] = heatLoss
                predecessors[neighbor] = _min

                q[neighbor] = heatLoss # we need to visit neighbor's neighors
    
    return (predecessors, distances)

def findEnd(distances):
    # find node matching end position with minimal distance
    endNode = None
    endDist = inf
    for node, d in distances.items():
        x, y, _ = node
        if (x, y) == end:
            if d < endDist:
                endNode = node
                endDist = d
    return endNode

def makePath(predecessors, distances, endNode):
    path = [endNode]
    while not (path[-1][0] == 0 and path[-1][1] == 0):
        path.append(predecessors[path[-1]])

    path.reverse()

    path = [(x, y) for x, y, _ in path]
    return path


start = (0, 0)
end = (W -1, H -1)

# part 1
MIN_JUMP, MAX_JUMP = 1, 3
predecessors, distances = dijkstra(data, start, end, MIN_JUMP, MAX_JUMP)
endNode = findEnd(distances)

print(distances[endNode])

if utils.DEBUG:
    path = makePath(predecessors, distances, endNode)
    printPath(data, path)
    assert distances[endNode] == 102
else:
    assert distances[endNode] == 638

# part 2
MIN_JUMP, MAX_JUMP = 4, 10
predecessors, distances = dijkstra(data, start, end, MIN_JUMP, MAX_JUMP)
endNode = findEnd(distances)

print(distances[endNode])

if utils.DEBUG:
    path = makePath(predecessors, distances, endNode)
    printPath(data, path)
    assert distances[endNode] == 94
else:
    assert distances[endNode] == 748
