import utils
import numpy as np

# from sortedcontainers import *

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
motions = [l.split(' ') for l in inputLines]

# print(motions)

vectors = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

head = (0, 0)
tail = (0, 0)

headPositions = [(0, 0)]
tailPositions = [(0, 0)]
for motion in motions:
    direction = motion[0]
    count = int(motion[1])

    directionVector = vectors[direction]
    for i in range(count):
        # print(head, tail)
        head = np.add(head, directionVector)

        tailDirectionVector = (0, 0)

        if -1 <= head[0] - tail[0] <= 1 and -1 <= head[1] - tail[1] <= 1:
            tailDirectionVector = (0, 0)
        else:
            tailDirectionVector = (np.sign(head[0] - tail[0]), np.sign(head[1] - tail[1]))

        tail = np.add(tail, tailDirectionVector)
        headPositions.append(tuple(head))
        tailPositions.append(tuple(tail))

# print(headPositions)
# print(tailPositions)
print(len(set(tailPositions)))

tailPositions = [(0, 0)]
snake = [(0, 0)] * 10
for motion in motions:
    direction = motion[0]
    count = int(motion[1])

    directionVector = vectors[direction]
    for i in range(count):
        # print(head, tail)
        head = np.add(snake[0], directionVector)
        snake[0] = tuple(head)

        for j in range(9):
            head = snake[j]
            tail = snake[j + 1]
            tailDirectionVector = (0, 0)

            if -1 <= head[0] - tail[0] <= 1 and -1 <= head[1] - tail[1] <= 1:
                tailDirectionVector = (0, 0)
            else:
                tailDirectionVector = (np.sign(head[0] - tail[0]), np.sign(head[1] - tail[1]))

            tail = np.add(tail, tailDirectionVector)
            snake[j + 1] = tail

        tailPositions.append(tuple(snake[-1]))

print(len(set(tailPositions)))
