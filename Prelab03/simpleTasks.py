#! /usr/bin/env python3.4

# Task 1
def find(pattern):
    # Read file
    with open('sequence.txt', 'r') as myFile:
    #with open('testseq.txt', 'r') as myFile:
        seq = myFile.read()
        len_seq = len(seq)
        len_pattern = len(pattern)
        i = 0
        j = 0
        perfect = []
        while 1:
            if seq[i] == pattern[j] or pattern[j] == "X":
                if j == 0:
                    found = seq[i]
                    i_return = i + 1
                else:
                    found = found + seq[i]
                i = i + 1
                j = j + 1
                if j == len_pattern:
                    perfect.append(found)
                    i = i_return
                    j = 0
                if i == len_seq:
                    return perfect
            else:
                if j == 0:
                    i = i + 1
                else:
                    i = i_return
                j = 0
                if i == len_seq:
                    return perfect

# Task 2
def getStreakProduct(sequence, maxSize, product):
    len_seq = len(sequence)
    i = 0
    perfect = []
    calculator = int(sequence[i])
    found = sequence[i]
    size = 1
    while 1:
        if size == 1:
            i_return = i + 1
        i = i + 1
        if i == len_seq:
            return perfect
        calculator = calculator * int(sequence[i])
        found = found + sequence[i]
        size = size + 1
        if size <= maxSize:
            if calculator == product:
                perfect.append(found)
                i = i_return
                calculator = int(sequence[i])
                found = sequence[i]
                size = 1
            if i + 1 == len_seq:
                i = i_return
                calculator = int(sequence[i])
                found = sequence[i]
                size = 1
        else:
            i = i_return
            calculator = int(sequence[i])
            found = sequence[i]
            size = 1
            if i == len_seq:
                return perfect

# Task 3
def writePyramids(filePath, baseSize, count, char):
    with open(filePath, 'w') as myFile:
        height = int((baseSize + 1) / 2)
        space_num1 = height - 1
        space_num2 = 1
        space_num3 = baseSize
        for i in range(height):
            for j in range(space_num1):
                myFile.write(" ")
            for k in range(count - 1):
                for l in range(space_num2):
                    myFile.write(char)
                for m in range(space_num3):
                    myFile.write(" ")
            for n in range(space_num2):
                myFile.write(char)
            for o in range(space_num1):
                myFile.write(" ")
            space_num1 = space_num1 - 1
            space_num2 = space_num2 + 2
            space_num3 = space_num3 - 2
            myFile.write("\n")

# Task 4
def getStreaks(sequence, letters):
    len_seq = len(sequence)
    perfect = []
    found = sequence[0]
    i = 1

    while 1:
        if i == len_seq:
            perfect.append(found)
            break
        if sequence[i] == sequence[i - 1]:
            found = found + sequence[i]
            i = i + 1
        else:
            perfect.append(found)
            found = sequence[i]
            i = i + 1
    # Find not needed sequence
    len_perfect = len(perfect)
    len_letters = len(letters)
    not_perfect = []
    for i in range(len_perfect):
        ok = 0
        for j in range(len_letters):
            if perfect[i][0] == letters[j]:
                ok = 1
        if ok == 0:
            not_perfect.append(perfect[i])
    # Remove not needed sequence
    len_not_perfect = len(not_perfect)
    for k in range(len_not_perfect):
        perfect.remove(not_perfect[k])

    return perfect

# Task 5
def findNames(nameList, part, name):
    firstnameList = []
    lastnameList = []
    perfect = []
    len_nameList = len(nameList)
    for i in range(len_nameList):
        full_name = nameList[i]
        name_split = full_name.split()
        firstnameList.append(name_split[0])
        lastnameList.append(name_split[1])
    if part == "L":
        for i in range(len_nameList):
            if lastnameList[i].lower() == name.lower():
                perfect.append(nameList[i])

    elif part == "F":
        for i in range(len_nameList):
            if firstnameList[i].lower() == name.lower():
                perfect.append(nameList[i])

    elif part == "FL":
        for i in range(len_nameList):
            if lastnameList[i].lower() == name.lower() or firstnameList[i].lower() == name.lower():
                perfect.append(nameList[i])

    return perfect

# Task 6
def convertToBoolean(num, size):
    if type(num) != int or type(size) != int:
        return []
    num_in_binary = bin(num)[2:]
    num_in_binary_zero_filled = num_in_binary.zfill(size)
    perfect = []
    len_binary = len(num_in_binary_zero_filled)
    for i in range(len_binary):
        if num_in_binary_zero_filled[i] == "1":
            perfect.append(True)
        elif num_in_binary_zero_filled[i] == "0":
            perfect.append(False)

    return perfect

# Task 7
def convertToInteger(boolList):
    if type(boolList) != type([]):
        return None
    elif boolList == []:
        return None
    len_boolList = len(boolList)
    perfect = 0
    i = len_boolList - 1
    power = 0
    while i >= 0:
        if boolList[i] == True:
            perfect = perfect + 2 ** power
            i = i - 1
            power = power + 1
        elif boolList[i] == False:
            i = i - 1
            power = power + 1
        else:
            return None

    return perfect

# Main Block (calls the functions above for testing)
if __name__ == "__main__":
    # calling functions
    ###1###
    print("PART 1")
    print(find("X8X88"))
    ###2###
    print("PART 2")
    print(getStreakProduct("14822446712422", 10, 32))
    print(getStreakProduct("54789654321687984", 10, 12))
    ###3###
    #writePyramids('test1.txt', 13, 7, 'X')
    #writePyramids('test2.txt', 15, 5, '*')
    ###4###
    print("PART 4")
    print(getStreaks("AAASSSSSSAPPPSSPPBBCCCSSS", "QPATS"))
    print(getStreaks("AAASSSSSSAPPPSSPPBBCCCSSS", "CCCBBB"))
    ###5###
    print("PART 5")
    print(findNames(["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"], "hjgk", "Johnson"))
    print(findNames(["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"], "L", "johnson"))
    print(findNames(["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"], "F", "JOHNSON"))
    print(findNames(["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"], "FL", "Johnson"))
    ###6###
    print("PART 6")
    print(convertToBoolean(9, 3))
    print(convertToBoolean(135, 12))
    ###7###
    print("PART 7")
    print(convertToInteger([True, False, False, False, False, True, True, True]))
    print(convertToInteger([False, False, True, False, False, True]))
