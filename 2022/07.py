import utils

# from sortedcontainers import *

utils.DEBUG = True
utils.DEBUG = False
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())
# itemsList = utils.linesToChars(inputLines)
#
# print(utils.linesToNumbers(inputLines))
# print(utils.digitsInString(inputLines))

inputLines.pop(0)

print(inputLines)

path = ''
files = {}
folders = set()
folders.add('/')
for cmd in inputLines:
    if cmd.startswith('$'):
        if cmd.startswith('$ ls'):
            # print('ls')
            continue
        if cmd.startswith('$ cd'):
            if cmd.startswith('$ cd ..'):
                path = '/'.join(path.split('/')[:-1])
                # print('going to folder up path is ' + path)
            else:
                directory = cmd.split(' ')[2]
                path = path + '/' + directory
                # print('going to folder ' + dir + ' path is ' + path)
            continue
    size = cmd.split(' ')[0]
    name = cmd.split(' ')[1]
    fullName = path + '/' + name

    if size == 'dir':
        folders.add(fullName)
    else:
        files[fullName] = int(size)

folderSizes = {}
for folder in folders:
    fsize = 0
    for file, size in files.items():
        if file.startswith(folder):
            fsize += size
    folderSizes[folder] = fsize

s = 0

for _s in folderSizes.values():
    if _s < 100000:
        s += _s

print(files)
print(folderSizes)

goalSpace = 30000000

usedSpace = 0
for _s in files.values():
    usedSpace += _s

totalSpace = 70000000

toDelete = -(totalSpace - usedSpace - 30000000)

folderSizesList = list(folderSizes.values())
folderSizesList.sort()

print(f"Used space: {usedSpace}")
print(f"toDelete space: {toDelete}")

print(folderSizesList)

toDeleteFolderSpace = -1
for _s in folderSizesList:
    if _s >= toDelete and toDeleteFolderSpace == -1:
        toDeleteFolderSpace = _s

print(' ')
print('##########')
print(s)

print(toDeleteFolderSpace)
