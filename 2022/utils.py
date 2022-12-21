import os
import __main__
import datetime

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
def fileToLines(filePath):
    return open(filePath, 'r').read().splitlines()

