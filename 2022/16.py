import math
from queue import Queue
from itertools import permutations

import utils
import numpy as np

# utils.DEBUG = True
utils.printInfo()

inputLines = utils.fileToLines(utils.inputFilePath())


# backup
def _parseInput(inputLines):
    data = []
    for line in inputLines:
        words = line.split(' ')
        valve = words[1]
        flow = words[4].split('=')[1].split(';')[0]
        flow = int(flow)
        otherValves = tuple(map(lambda other: other.split(',')[0], words[9:]))
        data.append((valve, flow, otherValves))
    return data


def parseInput(inputLines):
    data = []
    valvesDict = {}

    # str -> int
    def getValve(name):
        if name in valvesDict.keys():
            return valvesDict[name]
        valvesDict[name] = len(valvesDict)
        return valvesDict[name]

    for line in inputLines:
        words = line.split(' ')
        valve = getValve(words[1])
        flow = words[4].split('=')[1].split(';')[0]
        flow = int(flow)
        otherValves = list(map(lambda other: other.split(',')[0], words[9:]))
        otherValves = tuple(map(getValve, otherValves))
        data.append((valve, flow, otherValves))

    return data, valvesDict


def dataToGraph(inputData):
    graph = {}
    for data in inputData:
        graph[data[0]] = list(data[2])
    return graph


def dataToPressures(inputData):
    p = {}
    for data in inputData:
        p[data[0]] = data[1]
    return p


def bfs(graph, source, keepSource=False):
    Q = Queue()
    distance = {k: math.inf for k in graph.keys()}
    visited_vertices = set()
    Q.put(source)
    visited_vertices.update({0})
    while not Q.empty():
        vertex = Q.get()
        if vertex == source:
            distance[vertex] = 0
        for u in graph[vertex]:
            if u not in visited_vertices:
                if distance[u] > distance[vertex] + 1:
                    distance[u] = distance[vertex] + 1
                Q.put(u)
                visited_vertices.update({u})
    if not keepSource:
        distance.pop(source)
    return distance


def bfss(inputData):
    distances = {}
    g = dataToGraph(inputData)
    for data in inputData:
        d = bfs(g, data[0])
        distances[data[0]] = d
    return distances


# part 1
inputData, valveDict = parseInput(inputLines)
distances = bfss(inputData)
pressures = dataToPressures(inputData)

# minute (max 30 inc), pressure, pos, opened valves
paths = [[1, 0, valveDict['AA'], set()]]
validPressures = {0}
while len(paths) > 0:
    newPaths = []
    for path in paths:
        time, pressure, pos, visited = path
        if time > 30:
            continue
        validPressures.add(pressure)

        # move and open
        for destination, d in distances[pos].items():
            if destination in visited:
                continue
            flow = pressures[destination]
            if flow == 0:
                continue
            remainingTime = 30 - time - d
            valvePressure = flow * remainingTime
            newVisited = visited.copy()
            newVisited.add(destination)
            np = [time + d + 1, pressure + valvePressure, destination, newVisited]
            newPaths.append(np)
    paths = newPaths
print("PART1")
print(max(validPressures))

# part 1
inputData, valveDict = parseInput(inputLines)
distances = bfss(inputData)
pressures = dataToPressures(inputData)

# minute (max 26 inc), timeElephant, pressure, pos, posElephant, opened valves
paths = [[1, 1, 0, valveDict['AA'], valveDict['AA'], set()]]
visitedStates = set()
validPressures = {0}
while len(paths) > 0:
    newPaths = []
    for path in paths:
        time, time2, pressure, pos, posElephant, visited = path
        visitedStates.add((time, time2, pressure, pos, posElephant, frozenset(visited)))
        validPressures.add(pressure)

        # move and open
        if time <= 26:
            for destination, d in distances[pos].items():
                if destination in visited:
                    continue
                flow = pressures[destination]
                if flow == 0:
                    continue
                newTime = time + d + 1
                if newTime > 26:
                    continue
                remainingTime = 26 - time - d
                valvePressure = flow * remainingTime
                newVisited = visited.copy()
                newVisited.add(destination)
                p2 = pressure + valvePressure
                np = [newTime, time2, p2, destination, posElephant, newVisited]
                if (newTime, time2, p2, destination, posElephant, frozenset(newVisited)) not in visited:
                    newPaths.append(np)

        if time2 <= 26:
            for destination, d in distances[posElephant].items():
                if destination in visited:
                    continue
                flow = pressures[destination]
                if flow == 0:
                    continue
                newTime = time2 + d + 1
                if newTime > 26:
                    continue
                remainingTime = 26 - time2 - d
                valvePressure = flow * remainingTime
                newVisited = visited.copy()
                newVisited.add(destination)
                p2 = pressure + valvePressure
                np = [time, newTime, pressure + valvePressure, pos, destination, newVisited]
                if (time, newTime, pressure + valvePressure, pos, destination, frozenset(newVisited)) not in visited:
                    newPaths.append(np)

    paths = newPaths
print("PART2")
print(max(validPressures))
