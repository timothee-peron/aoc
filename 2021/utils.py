import os
import __main__

DEBUG = False


# script utils

def runningFileName():
    return os.path.splitext(os.path.basename(__main__.__file__))[0]


def inputFilePath():
    rfn = runningFileName()
    folder = "samples" if DEBUG else "inputs"
    return folder + "/" + rfn + ".txt"


def fileToLString(filePath):
    return open(filePath, 'r').read()


def fileToLines(filePath):
    return open(filePath, 'r').read().splitlines()


def groupListByN(_list, n):
    return list(zip(*(iter(_list),) * n))
