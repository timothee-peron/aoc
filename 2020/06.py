import utils

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLString(utils.inputFilePath()).split('\n\n')

charsSet = [set(list(l)) for l in inputLines]
for s in charsSet:
    s.discard('\n')

print(sum(map(len, charsSet)))

cnts = []
for line in inputLines:
    answers = line.split('\n')
    s = None

    for answer in answers:
        _s = set(list(answer))
        if s is None:
            s = _s
        else:
            s = s & _s
    
    cnts.append(len(s))

print(sum(cnts))
