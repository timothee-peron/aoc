import utils

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLString(utils.inputFilePath())
dataChunks = inputLines.split('\n\n')

seedsLine = dataChunks[0]
mapLines = dataChunks[1:]

seeds = list(map(int, seedsLine.split(' ')[1:]))

transforms = [[list(map(int,y.split(' '))) for y in x.split('\n')[1:] ]  for x in mapLines]

nextSeed = list(seeds)
for transform in transforms:
    for i, s in enumerate(nextSeed):
        for dest, src, rang in transform:
            if src <= s < src + rang:
                nextSeed[i] = dest + s - src
                break

print(min(nextSeed))

seedRanges = list(zip(seeds[::2], seeds[1::2]))

ranges = list(seedRanges)
for transform in transforms:
    nextRanges = []
    while len(ranges) > 0:
        s, l = ranges.pop()

        for dest, src, rang in transform:
            if src <= s < src + rang:
                d = dest + s - src
                if s + l <= src + rang:
                    nextRanges.append((d, l))
                else:
                    l1 = src + rang - s
                    nextRanges.append((d, l1))
                    ranges.append((src + rang, l - l1))
                break

    ranges = list(nextRanges)

print(min(map(lambda x:x[0], ranges)))
