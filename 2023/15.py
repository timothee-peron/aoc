import utils
from functools import cache

# utils.DEBUG = True
utils.printInfo()

data = utils.fileToLString(utils.inputFilePath()).strip()

@cache
def HASH (str):
    x = 0
    for c in str:
        x += ord(c)
        x *= 17
        x %= 256
    return x

assert HASH('HASH') == 52

# part 1
print(sum(map(HASH, data.split(','))))

# part 2
b = [{} for _ in range(256)]
def HASHMAP(boxes, instruction):
    if instruction.endswith('-'):
        x = instruction.split('-')[0]
        k = HASH(x)
        boxes[k].pop(x, None)
    else:
        x, y = instruction.split('=')
        y = int(y)
        k = HASH(x)
        if x in boxes[k].keys():
            # python replaces keys keeping order of insertion
            boxes[k][x] = y
        else:
            # python keeps keys in order of insertion
            boxes[k][x] = y

for i in data.split(','):
    HASHMAP(b, i)

scores = []
for i, box in enumerate(b):
    for j, (k, v) in enumerate(box.items()):
        scores.append((i + 1) * (j + 1) * v)

print(sum(scores))
