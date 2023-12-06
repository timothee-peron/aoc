import utils

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())

data = []
for line in inputLines:
    wins, actual = line.split(' | ')
    wins = wins.split(': ')[1]
    wins = wins.split(' ')
    actual = actual.split(' ')
    wins = list(filter(lambda x: x!='', wins))
    actual = list(filter(lambda x: x!='', actual))
    wins = list(map(int, wins))
    actual = list(map(int, actual))
    data.append((wins, actual))

scores = []
for wins, actual in data:
    _w = set(wins)
    _a = set(actual)
    wins = list(_w & _a)
    if len(wins) > 0:
        scores.append(2**(len(wins)-1))
    else:
        scores.append(0)

print(sum(scores))

N = len(inputLines)

wins = []
for w, actual in data:
    _w = set(w)
    _a = set(actual)
    __w = list(_w & _a)
    wins.append(len(__w))

cards = [1 for _ in range(N)]
for i, w in enumerate(wins):
    for j in range(w):
        if (i + j) < N:
            cards[i + j + 1] += cards [i]

print(sum(cards))
