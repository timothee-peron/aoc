import os

inputFileDir = os.path.dirname(__file__)
inputFileName = "01.txt"
inputFileName = "01.txt"

inputFileFullDir = os.path.join(inputFileDir, inputFileName)

def readInputFile(filePath):
  return open(filePath,'r').read().splitlines()

def makeInputMap(lines):
  map = []
  for l in lines:
    letters = list(l)
    map.append([int(letter) for letter in letters])
  return map


inputLines = readInputFile(inputFileFullDir)
inputMap = makeInputMap(inputLines)

# CONSTANT : size (x, y) or (w, h)
inputSize = (len(inputMap[0]), len(inputMap))

# ----> x
# |
# |
# ^ y
def getValueAt(_map, _x, _y):
  if(_x >= 0 and _x < inputSize[0] and _y >= 0 and _y < inputSize[1]):
    value = _map[_y][_x]
    return value
  return None

def getAdjacentValues(_map, _x, _y):
  results = []
  points = [(_x, _y+1),(_x, _y-1),(_x+1, _y),(_x-1, _y)]
  for point in points:
    value = getValueAt(_map, point[0], point[1])
    if value is not None:
      results.append(value)
  return results

def getLowPoints(_map):
  lows = []
  for y in range(inputSize[1]):
    for x in range(inputSize[0]):
      val = getValueAt(_map, x, y)
      adj = getAdjacentValues(_map, x, y)
      if(val < min(adj)):
        lows.append((x,y))
  return lows

def computeRiskLevel(_map, lows):
  risks = []
  for low in lows:
    val = getValueAt(_map, low[0], low[1])
    risks.append(val + 1)
  return risks

lowPoints = getLowPoints(inputMap)
print(sum(computeRiskLevel(inputMap, lowPoints)))

def getAdjacentBasinCoordinates(_map, _x, _y):
  results = []
  points = [(_x, _y+1),(_x, _y-1),(_x+1, _y),(_x-1, _y)]
  for point in points:
    value = getValueAt(_map, point[0], point[1])
    if value is not None and value != 9:
      results.append((point[0], point[1]))
  return results


def findBassin(_map, low):
  explored = [low]
  toExploreFrom = [[low, getAdjacentBasinCoordinates(_map, low[0], low[1])]]

  while len(toExploreFrom) > 0:
    newToExploreFrom = []
    for flowingTo, toExplore in toExploreFrom:
      valueAtFrom = getValueAt(_map, flowingTo[0], flowingTo[1])
      for p in toExplore:
        valueAtTo = getValueAt(_map, p[0], p[1])
        if valueAtTo > valueAtFrom:
          if p not in explored:
            explored.append(p)
          adjacent = getAdjacentBasinCoordinates(_map, p[0], p[1])
          _adj = list(filter(lambda x: x not in explored, adjacent))
          if len(_adj) > 0:
            newToExploreFrom.append([p, _adj])
    toExploreFrom = newToExploreFrom
  return explored

bassins = list(map(lambda p: len(findBassin(inputMap, p)), lowPoints))

bassins.sort(reverse = True)
print(bassins[0] * bassins[1] * bassins[2] )
