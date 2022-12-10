import numpy as np
import utils

utils.DEBUG = True
utils.DEBUG = False
inputFileFullDir = utils.inputFilePath()


def readInputFile(filePath):
    return open(filePath, 'r').read()


_file = readInputFile(inputFileFullDir).split('\n\n')
dots = [list(map(lambda x: int(x), i.split(','))) for i in _file[0].split('\n')]
instructions = [(i.split(' ')[2].split('=')[0], int(i.split(' ')[2].split('=')[1])) for i in _file[1].split('\n')]

print(dots)
print(instructions)

maxX = max(map(lambda i: i[0], dots)) + 1
maxY = max(map(lambda i: i[1], dots)) + 1

print(f'size is {maxX} x {maxY}')

dots_map = np.zeros((maxY, maxX))

for (x, y) in dots:
    dots_map[y, x] = 1


def fold(_m, axis, value):
    if axis == 'x':
        __m = np.hsplit(_m, [value, value + 1])
        (m1, ___m, m2) = __m
        pad = np.shape(m1)[1] - np.shape(m2)[1]
        if pad > 0:
            m2 = np.pad(m2, [(0, 0), (0, pad)], mode='constant', constant_values=0)
        if pad < 0:
            m1 = np.pad(m1, [(0, 0), (-pad, 0)], mode='constant', constant_values=0)
        m2 = np.fliplr(m2)
        return np.add(m1, m2)
    if axis == 'y':
        __m = np.vsplit(_m, [value, value + 1])
        (m1, ___m, m2) = __m
        pad = np.shape(m1)[0] - np.shape(m2)[0]
        if pad > 0:
            m2 = np.pad(m2, [(0, pad), (0, 0)], mode='constant', constant_values=0)
        if pad < 0:
            m1 = np.pad(m1, [(-pad, 0), (0, 0)], mode='constant', constant_values=0)
        m2 = np.flipud(m2)
        return np.add(m1, m2)


step1 = np.copy(dots_map)
for instruction in instructions:
    step1 = fold(step1, instruction[0], instruction[1])
    break;

numDots = 0
for y in step1:
    for x in y:
        if x > 0:
            numDots += 1
print("step1: " + str(numDots))

step2 = np.copy(dots_map)
for instruction in instructions:
    step2 = fold(step2, instruction[0], instruction[1])

print('step2:')
for y in step2:
    for x in y:
        if x > 0:
            print('<>', end='')
        else:
            print('  ', end='')
    print('')
