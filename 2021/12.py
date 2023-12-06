from collections import defaultdict
import utils

# utils.DEBUG = True
inputFileFullDir = utils.inputFilePath()


def readInputFile(filePath):
    return open(filePath, 'r').read().splitlines()


inputlines = readInputFile(inputFileFullDir)
edges = frozenset([frozenset(x.split('-')) for x in inputlines])
nodes = set([x.split('-')[0] for x in inputlines]).union(set([x.split('-')[1] for x in inputlines]))

print(edges)
print(nodes)


def getVoisins(node):
    listVoisins = set()
    for edge in edges:
        if node in edge:
            remains = edge.difference({node})
            listVoisins.add(list(remains)[0])
    listVoisins.discard('start')
    return listVoisins


def getSmallCaves(path):
    sc = set()
    for node in path:
        if node.islower() and node != 'start' and node != 'end':
            sc.add(node)
    return sc


def getSmallCavesWithNum(path):
    def def_value():
        return 0

    sc = defaultdict(def_value)
    for node in path:
        if node.islower() and node != 'start' and node != 'end':
            sc[node] += 1
    return sc


notCompletePathChecker = lambda x: x[-1] != 'end'
completePathChecker = lambda x: x[-1] == 'end'

allSmallCaves = getSmallCaves(list(nodes))

paths = [['start', x] for x in getVoisins('start')]
while len(list(filter(notCompletePathChecker, paths))) > 0:
    nextStepPaths = list(filter(completePathChecker, paths))
    for path in list(filter(notCompletePathChecker, paths)):
        smallCaves = getSmallCaves(path)
        voisins = getVoisins(path[-1])
        for voisin in voisins:
            if voisin in smallCaves:
                continue

            newPath = [n for n in path]
            newPath.append(voisin)
            nextStepPaths.append(tuple(newPath))
    paths = list(dict.fromkeys(nextStepPaths))

print(len(paths))

# exit(0)

paths = [['start', x] for x in getVoisins('start')]
while len(list(filter(notCompletePathChecker, paths))) > 0:
    nextStepPaths = list(filter(completePathChecker, paths))
    for path in list(filter(notCompletePathChecker, paths)):
        smallCaves = getSmallCavesWithNum(path)
        smallCavesSet = getSmallCaves(path)
        voisins = getVoisins(path[-1])
        for voisin in voisins:
            if voisin in smallCavesSet and 2 in smallCaves.values():
                continue

            newPath = [n for n in path]
            newPath.append(voisin)
            nextStepPaths.append(tuple(newPath))
    paths = list(dict.fromkeys(nextStepPaths))

print(len(paths))
