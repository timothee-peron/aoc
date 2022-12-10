import utils

utils.DEBUG = True
utils.DEBUG = False

inputLines = utils.fileToLines(utils.inputFilePath())
# wholeFile = utils.fileToLString(utils.inputFilePath())

measures = list(map(lambda x: int(x), inputLines))

print("part1")

increased = 0
stack = []
for measure in measures:
    stack.append(measure)
    if len(stack) > 2:
        stack.pop(0)

    if len(stack) < 2:
        continue

    if stack[1] > stack[0]:
        increased += 1

print(increased)

print("part2")

increased = 0
stack = []
for measure in measures:
    stack.append(measure)
    if len(stack) > 4:
        stack.pop(0)

    if len(stack) < 4:
        continue
    if sum(stack[:3]) < sum(stack[-3:]):
        increased += 1

print(increased)
