import utils

# utils.DEBUG = True
utils.printInfo()

data = [list(x) for x in utils.fileToLines(utils.inputFilePath())]

H = len(data)
W = len(data[0])

allowedDirections = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]

allX = set((x, y) for x in range(W) for y in range(H) if data[y][x] == 'X')
allM = set((x, y) for x in range(W) for y in range(H) if data[y][x] == 'M')
allA = set((x, y) for x in range(W) for y in range(H) if data[y][x] == 'A')
allS = set((x, y) for x in range(W) for y in range(H) if data[y][x] == 'S')

count = 0
for (xx, yx) in allX:
  dx, dy = (0,0)
  for (xm, ym) in allM:
    if abs(xm -xx) <= 1 and abs(ym -yx) <= 1:
      dx, dy = (xm - xx, ym -yx)
    else:
      continue
    
    xa, ya = (xm + dx, ym + dy)
    xs, ys = (xa + dx, ya + dy)

    count += 1 if (xa, ya) in allA and (xs, ys) in allS else 0

print(count)

centers = set()
count = 0
for (xm, ym) in allM:
  for (xa, ya) in allA:
    if (xa, ya) in centers:
      continue

    if abs(xa -xm) == 1 and abs(ya -ym) == 1:
      dx, dy = (xa - xm, ya - ym)
      
      xs, ys = (xa + dx, ya + dy)
      if (xs, ys) in allS:
        u, v = (dx, -dy)
        w, z = (-dx, dy)

        p1x, p1y = (xa + u, ya + v)
        p2x, p2y = (xa + w, ya + z)

        if (p1x, p1y) in allM and (p2x, p2y) in allS:
          count += 1
          centers.add((xa, ya))
        if (p1x, p1y) in allS and (p2x, p2y) in allM:
          count += 1
          centers.add((xa, ya))

print(count)
