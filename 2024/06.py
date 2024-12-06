import utils
import functools

# utils.DEBUG = True
utils.printInfo()

data = utils.fileToLString(utils.inputFilePath()).strip()
data = list(list(l) for l in data.split('\n'))
H = len(data)
W = len(data[0])

def findGpos(d):
  for (y, l) in enumerate(d):
    for (x, c) in enumerate(l):
      if c == "^":
        return (x, y)
  raise Exception("NOT OK")

def findObstacle(d):
  obs = set()
  for (y, l) in enumerate(d):
    for (x, c) in enumerate(l):
      if c == "#":
        obs.add((x, y))
  return obs

def move(posG, direc, obstacles):
  px, py = posG
  u, v = direc
  x, y = px + u, py + v
  if (x, y) not in obstacles:
    return ((x, y), direc)
  
  if direc == (0, -1):
    return (posG, (1, 0))
  if direc == (1, 0):
    return (posG, (0, 1))
  if direc == (0, 1):
    return (posG, (-1, 0))
  if direc == (-1, 0):
    return (posG, (0, -1))

  raise Exception("NOT OK")

posgard = findGpos(data)
obstacles = findObstacle(data)
direction = (0, -1)

markPos = {posgard}
while (True):
  posgard, direction = move(posgard, direction, obstacles)

  if not ( 0 <= posgard[0] < W and 0 <= posgard[1] < H):
    break

  markPos.add(posgard)

print(len(markPos))

def isAloop(posG, direc, obstacles):
  markPosDir = set()

  while (True):
    posG, direc = move(posG, direc, obstacles)

    if not ( 0 <= posG[0] < W and 0 <= posG[1] < H):
      return False
    
    if( (posG, direc) in markPosDir):
      return True

    markPosDir.add((posG, direc))

cntLoops = 0
g = findGpos(data)
d = (0, -1)
for (y, l) in enumerate(data):
  for (x, c) in enumerate(l):
    if (c == '.'):
      obs = findObstacle(data)
      obs.add((x,y))
      if(isAloop(g,d,obs)):
        cntLoops += 1
print(cntLoops)

