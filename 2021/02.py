import utils
import numpy as np

# utils.DEBUG = True

inputLines = utils.fileToLines(utils.inputFilePath())
# wholeFile = utils.fileToLString(utils.inputFilePath())

measures = [(line.split(' ')[0], int(line.split(' ')[1])) for line in inputLines]

dic = {
    'forward': (1, 0),
    'down': (0, 1),
    'up': (0, -1)
}

pos = (0, 0)
for measure in measures:
    direction, value = measure
    vector = np.array(dic[direction]) * value
    pos = np.add(pos, vector)

print("part1")
print(np.prod(pos))

dic = {
    'down': 1,
    'up': -1,
}

# aim x depth
pos = [0, 0, 0]
for measure in measures:
    direction, value = measure

    if direction == "forward":
        pos[1] += value
        pos[2] += pos[0] * value
        continue

    pos[0] += dic[direction] * value

print("part2")
print(pos[1] * pos[2])
