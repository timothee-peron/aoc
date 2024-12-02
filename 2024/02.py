import utils

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
inputMap = [[int(x) for x in line.split(' ')] for line in inputLines]

def isSafe(line):
  if line[0] == line[1]:
    return False
  isIncreasing = line[0] < line[1]
  line = line if isIncreasing else list(reversed(line))

  pairs = [(line[i], line[i+1]) for i in range(len(line) - 1)]
  for x, y in pairs:
    if not 0 < y - x <= 3:
      return False
  
  return True

print(sum(map(isSafe, inputMap)))

def isSafeDampened(line):
  for i in range(len(line)):
    if isSafe([line[j] for j in range(len(line)) if j != i]):
      return True
  return False

print(sum(map(isSafeDampened, inputMap)))
