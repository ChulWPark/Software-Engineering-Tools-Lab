#! /user/local/bin/python3.4

from moduleTasks import *

# Part 3
def loadMultiple(signalNames, folderName, maxCount):
    perfect = {}
    for signal in signalNames:
        try:
            info = loadDataFrom(signal, folderName)
        except ValueError:
            perfect[signal] = None
        except OSError:
            perfect[signal] = None
        else:
            info = loadDataFrom(signal, folderName)
            floatlist = info[0]
            nonfloatcount = info[1]
            if nonfloatcount <= maxCount:
                perfect[signal] = floatlist
            elif nonfloatcount > maxCount:
                perfect[signal] = []

    return perfect

def saveData(signalsDictionary, targetFolder, bounds, threshold):
    for signal in signalsDictionary:
        # If it's an acceptable signal
        if signalsDictionary[signal] != []:
            # If the number of float values outside the valid range is less than or equal to the acceptable maximum value
            if isBounded(signalsDictionary[signal], bounds, threshold):
                # Write that signal to the target folder
                path = targetFolder + "/" + signal + ".txt"
                with open(path, 'w') as myFile:
                    for value in signalsDictionary[signal]:
                        myFile.write("{0:.3f}".format(value))
                        if value != signalsDictionary[signal][-1]:
                            myFile.write("\n")

# Conditional Main Block
if __name__ == "__main__":
    print("-----PART3-----")
    print("loadMultiple testing... (signal name is not valid)")
    print(loadMultiple(["abc123"], "Signals", 5))
    print("loadMultiple testing... (signal file doesn't exist)")
    print(loadMultiple(["ABC-123"], "Signals", 5))
    print("loadMultiple testing...")
    print(loadMultiple(["AFW-481", "GUO-758", "ISO-610"], "Signals", 5))
    print("saveData testing...")
    perfect = loadMultiple(["AFW-481", "GUO-758", "ISO-610"], "Signals", 5)
    saveData(perfect, "empty", (-12, 12), 5)
