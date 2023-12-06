import utils

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())

allGames = {}

for line in inputLines:
    (gid, games) = line.split(': ')
    gid = int(gid.split(' ')[1])

    rounds = []
    for game in games.split('; '):
        _round = {}
        for dice in game.split(', '):
            (num, color) = dice.split(' ')
            num = int(num)
            _round[color] = num
        rounds.append(_round)
    allGames[gid] = rounds

maxdice = {'red': 12, 'green': 13, 'blue': 14}

def validRound(_round, _maxd):
    for _color, _maxnum in _maxd.items():
        if _color in _round.keys() and _round[_color] > _maxnum:
            return False
    return True

def validGame(_game, _maxd):
    for _round in _game:
        if not validRound(_round, _maxd):
            return False
    return True

# part 1

validGames = []
for gid, game in allGames.items():
    if validGame(game, maxdice):
        validGames.append(gid)
print(sum(validGames))

# part 2

def minRoundDice(_round):
    vals = {'green' : 0, 'red': 0, 'blue': 0}
    for _color, _maxnum in vals.items():
        if _color in _round.keys():
            vals[_color] = _round[_color]
    return vals

def minGameDive(_game):
    vals = {'green' : 0, 'red': 0, 'blue': 0}
    for _round in _game:
        toAdd = minRoundDice(_round)
        for _color, val in toAdd.items():
            if val > vals[_color]:
                vals[_color] = val
    return vals

# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
# The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively.
# Adding up these five powers produces the sum 2286.

def power(_dices):
    p = 1
    for _dice in _dices.values():
        p *= _dice
    return p

assert(power({'r':4, 'g':2, 'b':6}) == 48)

scores = []
for gid, game in allGames.items():
    dices = minGameDive(game)
    scores.append(power(dices))
print(sum(scores))
