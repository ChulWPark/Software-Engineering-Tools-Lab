#! /user/local/bin/python3.4

from simpleVector import *

def loadVectors(fileName):
    perfect = []
    with open(fileName, 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            line = line.strip()
            try:
                vec = Vector(line)
            except:
                perfect.append(None)
            else:
                perfect.append(vec)
    return perfect

if __name__ == "__main__":
    perfect = loadVectors("values.txt")
    print(perfect)
