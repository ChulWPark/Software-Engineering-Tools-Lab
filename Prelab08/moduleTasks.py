#! /user/local/bin/python3.4

from exModule import runNetworkCode
import re
import os

# PART 1
def checkNetwork(**kwargs):
    try:
        runNetworkCode(**kwargs)
    except ConnectionError:
        raise ConnectionError
    except OSError as e:
        msg = "An issue encountered during runtime. The name of the error is: " + type(e).__name__
        return msg
    except:
        return False
    else:
        return True

# PART 2
def isOK(signalName):
    m = re.match(r"[A-Z]{3}-[0-9]{3}", signalName)
    if m == None:
        return False
    else:
        return True

def loadDataFrom(signalName, folderName):
    # If the signal name is invalid, raise a ValueError
    if isOK(signalName) == False:
        msg = signalName + " is invalid."
        raise ValueError(msg)
    # If the signal name is valid, but the file is not present in the signalFolder, raise an OSError
    fileName = signalName + ".txt"
    for noneed1, noneed2, signalFiles in os.walk(folderName):
        if fileName not in signalFiles:
            msg = fileName + " is not present in " + folderName + " folder."
            raise OSError(msg)
    # Normal Operation
    nonfloatcount = 0
    floatlist = []
    path = folderName + "/" + fileName
    with open(path, 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            m = re.match(r"[-]?[0-9]+[.][0-9]+", line)
            if m == None:
                nonfloatcount = nonfloatcount + 1
            else:
                floatlist.append(float(m.group(0)))
    
    return tuple([floatlist, nonfloatcount])
    
def isBounded(signalValues, bounds, threshold):
    # If the signal contains no values, raise a ValueError
    if signalValues == []:
        raise ValueError("Signal contains no data.")
    # Normal Operation
    lo = float(bounds[0])
    hi = float(bounds[1])
    obcount = 0
    for value in signalValues:
        if value < lo or value > hi:
            obcount = obcount + 1
    if obcount <= threshold:
        return True
    else:
        return False

# Conditional Main Block
if __name__ == "__main__":
    print("-----PART1-----")
    print("Throwing OSError testing...")
    print(checkNetwork(ose="park"))
    #print("Throwing Connection Error testing...")
    #print(checkNetwork(cone="park"))
    print("Throwing any other exception testing... (ValueError)")
    print(checkNetwork(anye="park"))
    print("Throwing no exception testing... (pass)")
    print(checkNetwork(noe="park"))
    print("-----PART2-----")
    print("isOK testing... (DAS-900)")
    print(isOK("DAS-900"))
    print("isOK testing... (SWE-314)")
    print(isOK("SWE-314"))
    print("isOK testing... (abc-123)")
    print(isOK("abc-123"))
    print("isOK testing... (a-1)")
    print(isOK("a-1"))
    print("isOK testing... (abc123)")
    print(isOK("abc123"))
    #print("loadDataFrom testing... (bad signal name)")
    #print(loadDataFrom("abc123", "folderName"))
    #print("loadDataFrom testing... (non-existing signalFile)")
    #print(loadDataFrom("DAS-900", "Signals"))
    print("loadDataFrom testing... (existing signalfile)")
    print(loadDataFrom("AFW-481", "Signals"))
    #print("isBounded testing... (empty signalValues)")
    #print(isBounded([], (-12, 12), 5))
    print("isBounded testing...")
    perfect = loadDataFrom("AFW-481", "Signals")
    print(isBounded(perfect[0], (-12, 12), 5))
