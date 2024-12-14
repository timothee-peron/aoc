import utils
import re
import math
from collections import defaultdict, deque

# utils.DEBUG = True
utils.printInfo()

INF = 1000000000

reCompiled = re.compile(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)")
def extractData(rawM):
  reResult = reCompiled.match(rawM)
  return {
    "A": (int(reResult.group(1)), int(reResult.group(2))),
    "B": (int(reResult.group(3)), int(reResult.group(4))),
    "C": (int(reResult.group(5)), int(reResult.group(6)))
  }

data = [extractData(machine.strip()) for machine in utils.fileToLString(utils.inputFilePath()).split('\n\n')]

# sub-optimal dijkstra
s = []
for m in data:
  xa,ya = m["A"]
  xb,yb = m["B"]
  xc,yc = m["C"]

  visited = set()
  distance = defaultdict(lambda: INF)
  previous = {}

  # x, y, pressA, pressB
  q = deque([(0,0,0,0)])

  while len(q) > 0:
    u = q.popleft()
    xu,yu,au,bu = u

    adjacents = []
    if au < 100:
      adjacents.append((xu+xa,yu+ya,au+1,bu))
    if bu < 100:
      adjacents.append((xu+xb,yu+yb,au,bu+1))

    for v in adjacents:
      xv,yv,av,bv = v
      visited.add((xv,yv))
      previousD = distance[(xv, yv)]
      newD = 3*av + bv
      if newD < previousD:
        distance[(xv, yv)] = newD
        previous[(xv, yv)] = (xu, yu, au, bu)
        q.append(v)
  
  if distance[(xc,yc)] != INF:
    s.append(distance[(xc,yc)])
print(sum(s))

# find the only integer solution
OFFSET = 10000000000000
s = []
for m in data:
  xa,ya = m["A"]
  xb,yb = m["B"]
  xc,yc = m["C"]
  xc += OFFSET
  yc += OFFSET

  alpha = ((xb*yc)-(yb*xc),(ya*xb)-(xa*yb))
  beta  = ((xa*yc)-(ya*xc),(yb*xa)-(xb*ya))

  if alpha[0] % alpha[1] == 0 and beta[0] % beta[1] == 0:
    s.append(3*(alpha[0] // alpha[1]) + (beta[0] // beta[1]))

print(sum(s))
