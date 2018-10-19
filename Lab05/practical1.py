#! /user/local/bin/python3.4

# PART I
def getHorizontalMax():
    # Initialize matrix
    matrix = []
    for i in range(20):
        matrix.append([])
    # Read off the file
    row = 0
    col = 0
    with open('square.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            split_line = line.split()
            for num in split_line:
                matrix[row].append(int(num))
            row = row + 1
    maximum = 0
    for i in range(20):
        for j in range(17):
            product = matrix[i][j] * matrix[i][j + 1] * matrix[i][j + 2] * matrix[i][j + 3]
            product_seq = [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2], matrix[i][j + 3]]
            if product > maximum:
                maximum = product
                max_sequence = product_seq
    
    perfect = tuple([maximum, max_sequence])
    return perfect

def getVerticalMax():
    # Initialize matrix
    matrix = []
    for i in range(20):
        matrix.append([])
    # Read off the file
    row = 0
    col = 0
    with open('square.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            split_line = line.split()
            for num in split_line:
                matrix[row].append(int(num))
            row = row + 1
    maximum = 0
    for i in range(20):
        for j in range(17):
            product = matrix[j][i] * matrix[j + 1][i] * matrix[j + 2][i] * matrix[j + 3][i]
            product_seq = [matrix[j][i], matrix[j + 1][i], matrix[j + 2][i], matrix[j + 3][i]]
            if product > maximum:
                maximum = product
                max_sequence = product_seq

    perfect = tuple([maximum, max_sequence])
    return perfect

# PART II
def getCode(name, day):
    valid = False
    date = []
    # Look for day
    with open("codes.txt", 'r') as myFile:
        all_lines = myFile.readlines()
        split_line = all_lines[1].split()
    # If date passed is not present in file
    if day not in split_line:
        return None
    # Find the index of that day
    j = 0
    for i in split_line:
        if i == day:
            index = j
        j = j + 1
    with open("codes.txt", 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines[3:]:
            split_line = line.split()
            name_target = split_line[0] + " " + split_line[1]
            if name_target == name:
                valid = True
                return str(split_line[index])
                
    if valid == False:
        return None

def getCodesOn(day):
    perfect = []
    # Look for day
    with open("codes.txt", 'r') as myFile:
        all_lines = myFile.readlines()
        split_line = all_lines[1].split()
    # If date passed is not present in file
    if day not in split_line:
        return set([])
    # Find the index of that day
    j = 0
    for i in split_line:
        if i == day:
            index = j
        j = j + 1
    with open("codes.txt", 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines[3:]:
            split_line = line.split()
            perfect.append(split_line[index])
    
    return set(perfect)

def getUsersOf(code):
    perfect = []
    # Look for day
    with open("codes.txt", 'r') as myFile:
        all_lines = myFile.readlines()
        split_line = all_lines[1].split()
    days = split_line
    with open("codes.txt", 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines[3:]:
            split_line = line.split()
            if code in split_line:
                a = 0
                for i in split_line:
                    if i == code:
                        index = a
                    a = a + 1
                name_target = split_line[0] + " " + split_line[1]
                perfect.append(tuple([name_target, days[index]]))
    
    return set(perfect)

def getCommonCodes(name1, name2):
    list1 = []
    list2 = []
    perfect = []
    with open("codes.txt", 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines[3:]:
            split_line = line.split()
            name_target = split_line[0] + " " + split_line[1]
            if name_target == name1:
                for code in split_line[2:]:
                    list1.append(code)
            elif name_target == name2:
                for code in split_line[2:]:
                    list2.append(code)
    for i in list1:
        if i in list2:
            perfect.append(i)

    return set(perfect)

if __name__ == "__main__":
    print("PART 1")
    print("HORIZONTAL")
    print(getHorizontalMax())
    print("VERTICAL")
    print(getVerticalMax())
    print("PART 2")
    print("getCode")
    print(getCode("Bailey, Catherine", "08/14"))
    print(getCode("Roberts, Teresa", "08/05"))
    print("getCodesOn")
    print(getCodesOn("08/18"))
    print(getCodesOn("08/25"))
    print("getUsersOf")
    print(getUsersOf("80860"))
    print(getUsersOf("111"))
    print(getUsersOf("99999"))
    print("getCommonCodes")
    print(getCommonCodes("Moore, John", "Ross, Frances"))
    print(getCommonCodes("Lee, Julie", "Thomas, Mark"))
    print(getCommonCodes("Brooks, Carol", "Smith, Jimmy"))
