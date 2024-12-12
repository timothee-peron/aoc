import utils
from collections import defaultdict, deque, Counter
from functools import cache

# utils.DEBUG = True
utils.printInfo()

data = list(list((y) for y in x) for x in utils.fileToLString(utils.inputFilePath()).split('\n'))

posPerLetter = defaultdict(set)
for y, line in enumerate(data):
  for x, c in enumerate(line):
    posPerLetter[c].add((x,y))

letterPerPos = {}
for y, line in enumerate(data):
  for x, c in enumerate(line):
    letterPerPos[(x,y)]=c

@cache
def adjacent(pos):
  xc, yc = pos
  return ((xc + 1, yc), (xc - 1, yc), (xc, yc + 1), (xc, yc - 1))

def getRegionSurface(r):
  return len(r)

def getRegionPerimeter(region):
  s = 0
  for pos in region:
    for x, y in adjacent(pos):
      if (x, y) not in region:
        s += 1
  return s

def getRegionLetter(region):
  return letterPerPos[next(iter(region))]

assert(getRegionSurface(set([(1,1)])) == 1)
assert(getRegionPerimeter(set([(1,1)])) == 4)
assert(getRegionPerimeter(set([(1,1), (1,2)])) == 6)

# find all regions
regions = []
explored = set()
for pos in letterPerPos.keys():
  if pos in explored:
    continue

  newRegion = set()
  regionLetter = letterPerPos[pos]
  exploredForRegion = set()

  q = deque([pos])
  while len(q) > 0:
    p = q.pop()
    c = letterPerPos[p]
    exploredForRegion.add(p)

    if c != regionLetter:
      continue

    newRegion.add(p)
    explored.add(p)

    for adj in adjacent(p):
      if adj in letterPerPos.keys() and adj not in explored and adj not in exploredForRegion:
        q.append(adj)
  
  regions.append(newRegion)

# for region in regions:
#   print(getRegionLetter(region), getRegionSurface(region), getRegionPerimeter(region), getRegionPerimeter(region) * getRegionSurface(region))

print(sum(getRegionPerimeter(region) * getRegionSurface(region) for region in regions))

def getSegments(positions):
  allPos = list(positions)
  if len(allPos) == 0:
    return 0

  allPos.sort()
  lastPos = -99
  segments = 1
  for x in allPos:
    if lastPos == -99:
      lastPos = x
      continue

    if lastPos + 1 != x:
      segments += 1
    lastPos = x
  return segments

assert(getSegments([]) == 0)
assert(getSegments([1]) == 1)
assert(getSegments([1, 2]) == 1)
assert(getSegments([1, 2, 3]) == 1)
assert(getSegments([1, 2, 3, 5, 6, 7]) == 2)

@cache
def adjacentH(pos):
  xc, yc = pos
  return ((xc, yc + 1, 1), (xc, yc, -1))
  
@cache
def adjacentV(pos):
  xc, yc = pos
  return ((xc + 1, yc, 1), (xc, yc, -1))

def getRegionNumberOfSides(region):
  s = 0
  segmentsH = []
  segmentsV = []
  for pos in region:
    for p in adjacentH(pos):
      segmentsH.append(p)
    
    for p in adjacentV(pos):
      segmentsV.append(p)

  filteredH = defaultdict(list)
  filteredV = defaultdict(list)
  for x, y, z in segmentsH:
    filteredH[(x, y)].append(z)
  for x, y, z in segmentsV:
    filteredV[(x, y)].append(z)

  allH = []
  for p, z in filteredH.items():
    if sum(z) != 0:
      x, y = p
      allH.append((x,y,sum(z)))
  allV = []
  for p, z in filteredV.items():
    if sum(z) != 0:
      x, y = p
      allV.append((x,y,sum(z)))
  
  s = 0
  # H
  for y in set(H for _, H, _ in allH):
    xs = [x for x, yy, z in allH if y == yy and z == 1]
    s += getSegments(xs)
    xs = [x for x, yy, z in allH if y == yy and z == -1]
    s += getSegments(xs)
  # V
  for x in set(V for V, _, _ in allV):
    ys = [y for xx, y, z in allV if x == xx and z == 1]
    s += getSegments(ys)
    ys = [y for xx, y, z in allV if x == xx and z == -1]
    s += getSegments(ys)

  return s

assert(getRegionNumberOfSides([(1,1)]) == 4)
assert(getRegionNumberOfSides([(1,1), (1,2)]) == 4)

# for region in regions:
#   print(getRegionLetter(region), getRegionSurface(region), getRegionNumberOfSides(region), getRegionNumberOfSides(region) * getRegionSurface(region))

print(sum(getRegionNumberOfSides(region) * getRegionSurface(region) for region in regions))