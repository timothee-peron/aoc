import utils
import functools

# utils.DEBUG = True
utils.printInfo()

rules, updates = utils.fileToLString(utils.inputFilePath()).split("\n\n")
rules = rules.strip().split("\n")
rules = set(tuple(int(i) for i in x.split('|')) for x in rules)
updates = [tuple(int(i) for i in x.split(',')) for x in updates.strip().split('\n')]

def isUpdateOk(data):
  for i in range(len(data)):
    for j in range(i + 1, len(data)):
      x, y = data[i], data[j]
      if (y, x) in rules:
        return False
  return True

def middleValue(data):
  return data[(len(data) - 1)//2]

print(sum(map(middleValue, filter(isUpdateOk, updates))))


def isUpdateKo(data):
  return not isUpdateOk(data)

def sorting(a, b):
  return -1 if (a,b) in rules else 1 if (b, a) in rules else 0

print(sum(map(middleValue, [sorted(l, key=functools.cmp_to_key(sorting)) for l in filter(isUpdateKo, updates)])))