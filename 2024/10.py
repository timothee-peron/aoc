import utils
from collections import defaultdict, deque

# utils.DEBUG = True
utils.printInfo()

data = list(list(int(y) for y in x) for x in utils.fileToLString(utils.inputFilePath()).split('\n'))

posPerH = defaultdict(set)
hPerPos = defaultdict(lambda: 99)
for y, l in enumerate(data):
    for x, h in enumerate(l):
        posPerH[h].add((x, y))
        hPerPos[(x,y)] = h


# part 1
score = 0
for start in posPerH[0]:
    # BSF
    q = deque([start])
    explored = defaultdict(lambda: False)
    distance = defaultdict(lambda: 99)
    distance[start] = 0
    explored[start] = True
    while len(q) > 0:
        ux, uy = q.popleft()
        h = hPerPos[(ux, uy)]
        for x, y in [(ux+1, uy), (ux-1, uy), (ux, uy+1), (ux, uy-1)]:
            if explored[(x, y)] or hPerPos[(x, y)] != h + 1:
                continue
            explored[(x,y)] = True
            distance[(x, y)] = h + 1
            q.append((x,y))
    for d in distance.values():
        if d == 9:
            score += 1
print(score)

# part 2
score = 0
for start in posPerH[0]:
    # BSF
    q = deque([start])
    explored = defaultdict(lambda: False)
    distance = defaultdict(lambda: 99)
    distance[start] = 0
    explored[start] = True
    predecessors = defaultdict(set)
    while len(q) > 0:
        ux, uy = q.popleft()
        h = hPerPos[(ux, uy)]
        for x, y in [(ux+1, uy), (ux-1, uy), (ux, uy+1), (ux, uy-1)]:
            if hPerPos[(x, y)] != h + 1:
                continue
            explored[(x,y)] = True
            distance[(x, y)] = h + 1
            predecessors[(x,y)].add((ux, uy))
            q.append((x,y))

    paths = set()
    for pos, d in distance.items():
        if d == 9:
            paths.add((pos,))
    
    for i in [8,7,6,5,4,3,2,1,0]:
        previousPath = {p for p in paths}
        paths = set()
        for p in previousPath:
            for node in predecessors[p[-1]]:
                newPath = list(A for A in p)
                newPath.append(node)
                paths.add(tuple(newPath))
    score += len(paths)

print(score)
