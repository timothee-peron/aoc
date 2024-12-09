import utils

# utils.DEBUG = True
utils.printInfo()

data = list(map(int, utils.fileToLString(utils.inputFilePath())))

expanded = []
isData = True
ID = 0
for n in data:
    if isData:
        for i in range(n):
            expanded.append(ID)
        ID += 1
    else:
        for i in range(n):
            expanded.append(-1)
    isData = not isData

i = 0
while i < len(expanded):
    while expanded[-1] == -1:
        expanded.pop()

    v = expanded[i]
    if v != -1:
        i+=1
        continue

    expanded[i] = expanded[-1]
    expanded.pop()

checksum = 0
for i, v in enumerate(expanded):
    checksum += i * v

print("Part 1")
print(checksum)

# part 2

print("Part 2")
print("This will take a few minutes...")

expanded = []
isData = True
ID = 0
for n in data:
    if isData:
        for i in range(n):
            expanded.append(ID)
        ID += 1
    else:
        for i in range(n):
            expanded.append(-1)
    isData = not isData

maxID = ID
for _id in reversed(range(maxID)):
    posToMove = []
    for j, v in enumerate(expanded):
        if v == _id:
            posToMove.append(j)
        elif len(posToMove) != 0:
            break
    
    destination = []
    for j, v in enumerate(expanded):
        if v == -1:
            destination.append(j)
        elif len(destination) != 0:
            if len(destination) < len(posToMove):
                destination = []
            else:
                break
    
    if len(destination) < len(posToMove):
        continue

    if posToMove[0] <= destination[0]:
        continue

    for j in range(len(posToMove)):
        expanded[destination[j]] = expanded[posToMove[j]]
        expanded[posToMove[j]] = -1

checksum = 0
for i, v in enumerate(expanded):
    if v == -1:
        continue
    checksum += i * v

print(checksum)
