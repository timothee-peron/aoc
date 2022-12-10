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
