#! /user/local/bin/python3.4

import os

def identifyAccess():
    perfect = {}
    for noneed1, noneed2, depFiles in os.walk("Departments"):
        for depFile in depFiles:
            depPath = "Departments/" + str(depFile)
            with open(depPath, 'r') as myFile:
                all_lines = myFile.readlines()
                for line in all_lines:
                    line = line.replace("\n", "")
                    if line not in perfect:
                        perfect[line] = []
                    perfect[line].append(depFile.replace(".txt", ""))
    for i in perfect:
        perfect[i].sort()

    return perfect

def getCommon(name1, name2):
    temp = []
    dictionary = identifyAccess()
    if name1 not in dictionary or name2 not in dictionary:
        return None
    list1 = dictionary[name1]
    list2 = dictionary[name2]
    for i in list1:
        if i in list2:
            temp.append(i)

    perfect = set(temp)
    return perfect

if __name__ == "__main__":
    print(identifyAccess())
    print(getCommon('wrongname', 'wrongname'))
    print(getCommon('Tamatha Granderson', 'Tasha Shell'))
    print(getCommon('Zenaida Blaisdell', 'Neomi Flournoy'))
    print(getCommon('Merideth Kind', 'Melba Gist'))
