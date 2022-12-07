import os
import __main__
import datetime
import re

DEBUG = False


# script utils

def runningFileName():
    return os.path.splitext(os.path.basename(__main__.__file__))[0]


def inputFilePath():
    rfn = runningFileName()
    folder = "samples" if DEBUG else "inputs"
    return folder + "/" + rfn + ".txt"


def printHorizontalLine(length):
    print("#" * length)


def printInfo():
    print()
    printHorizontalLine(100)
    print(f"Running {__main__.__file__} with input {inputFilePath()}")
    print(f"At: {str(datetime.datetime.now())}")
    printHorizontalLine(100)
    print()


# input utils


def fileToLString(filePath):
    return open(filePath, 'r').read()


def fileToLines(filePath):
    return open(filePath, 'r').read().splitlines()


def linesToItems(lines, splitter):
    return list(map(splitter, lines))


def linesToNumbers(lines):
    return list(map(lambda x: int(x), lines))


def linesToDigits(lines):
    _map = []
    for line in lines:
        letters = list(line)
        numbers = list(map(lambda x: int(x), letters))
        _map.append(numbers)
    return _map


def linesToChars(lines):
    _map = []
    for line in lines:
        letters = list(line)
        _map.append(letters)
    return _map


# string
# https://regexr.com/
def digitsInString(text):
    pattern = r"-?\d+"
    compiledRe = re.compile(pattern)
    results = compiledRe.findall(text)
    return results


def groupListByN(_list, n):
    return list(zip(*(iter(_list),) * n))
