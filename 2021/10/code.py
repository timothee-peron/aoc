import os

inputFileDir = os.path.dirname(__file__)
inputFileName = "01.txt"
inputFileName = "01.txt"

inputFileFullDir = os.path.join(inputFileDir, inputFileName)


def readInputFile(filePath):
    return open(filePath, 'r').read().splitlines()


def makeInputArr(lines):
    _map = []
    for l in lines:
        letters = list(l)
        _map.append(letters)
    return _map


pointsMap = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

closingChars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


# takes array of char as input
# returns True if ok or the invalid char
def validateLine(line):
    stackClosing = []
    for char in line:
        if char in closingChars.keys():
            stackClosing.append(closingChars[char])
        elif char in closingChars.values():
            if stackClosing[-1] == char:
                stackClosing.pop()
            else:
                return char
        else:
            raise Exception('Invalid char: ' + char)
    return stackClosing


inputLines = readInputFile(inputFileFullDir)
_input = makeInputArr(inputLines)

score = 0
for _line in _input:
    result = validateLine(_line)
    if type(result) == list:
        continue
    score += pointsMap[result]

print(score)

pointsMap = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

scores = []
for _line in _input:
    result = validateLine(_line)
    if type(result) != list:
        continue
    score = 0
    result.reverse()
    for cls in result:
        score = score*5 + pointsMap[cls]
    scores.append(score)
scores.sort()
print(scores[(len(scores) - 1)//2])
