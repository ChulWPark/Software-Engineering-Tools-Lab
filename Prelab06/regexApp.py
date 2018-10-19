#! /user/local/bin/python3.4

import re
from uuid import UUID

# PART 1
def getUrlParts(url):
    expr = r"http://(?P<BaseAddress>[\w.-]+)/(?P<Controller>[\w.-]+)/(?P<Action>[\w.-]+)"
    m = re.match(expr, url)
    
    return tuple([m.group("BaseAddress"), m.group("Controller"), m.group("Action")])

def getQueryParameters(url):
    perfect = []
    expr = r"[\w.-]+=[\w.-]+"
    found = re.findall(expr, url)
    for query in found:
        m = re.match(r"(?P<Field>[\w.-]+)=(?P<Value>[\w.-]+)", query)
        perfect.append(tuple([m.group("Field"), m.group("Value")]))
    
    return perfect

def getSpecial(sentence, letter):
    perfect = []
    # Find all words in a sentence
    expr = r"[\w]+"
    found = re.findall(expr, sentence)
    # Eliminate the words that both start and end with the letter
    remove = []
    for word in found:
        bothexpr = "^" + letter + ".*" + letter + "$"
        both = re.findall(bothexpr, word, re.I)
        if both != []:
            remove.append(both[0])
    for elem in remove:
        found.remove(elem)
    # Find all words that start or end with the letter
    for word in found:
        startexpr = "^" + letter + ".*$"
        endexpr = "^.*" + letter + "$"
        start = re.findall(startexpr, word, re.I)
        end = re.findall(endexpr, word, re.I)
        if start != [] or end != []:
            perfect.append(word)

    return perfect

def getRealMAC(sentence):
    expr = r"[0-9a-fA-F]{2}[:|-][0-9a-fA-F]{2}[:|-][0-9a-fA-F]{2}[:|-][0-9a-fA-F]{2}[:|-][0-9a-fA-F]{2}[:|-][0-9a-fA-F]{2}"
    found = re.findall(expr, sentence)
    if found != []:
        return found[0]
    else:
        return None    

# PART 2
def getRejectedEntries():
    perfect = []
    with open("Employees.txt", 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            expr = r"[\w]+[,]?[\s][\w]+"        # REGEX FOR NAME
            found = re.findall(expr, line)
            name = found[0]
            search = re.search(expr, line)
            found = re.findall(r"[\w]+", line[search.end():])
            if found == []:
                # If it's in <Last>, <First> format
                # Change into <First> <Last> format
                if re.search(r",", name):
                    m = re.match(r"(?P<Last>[\w]+), (?P<First>[\w]+)", name)
                    name = m.group("First") + " " + m.group("Last")
                perfect.append(name)
    perfect.sort()

    return perfect

def getEmployeesWithIDs():
    perfect = {}
    with open("Employees.txt", 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            expr = r"[\w]+[,]?[\s][\w]+"
            found = re.findall(expr, line)
            name = found[0]
            expr = r"[a-fA-F0-9]{8}[-]?[a-fA-F0-9]{4}[-]?[a-fA-F0-9]{4}[-]?[a-fA-F0-9]{4}[-]?[a-fA-F0-9]{12}"   # REGEX FOR ID
            found = re.findall(expr, line)
            if found != []:
                i = found[0]
                # If it's in <Last>, <First> format
                if re.search(r",", name):
                    m = re.match(r"(?P<Last>[\w]+), (?P<First>[\w]+)", name)
                    name = m.group("First") + " "  + m.group("Last")
                perfect[name] = str(UUID(i))

    return perfect

def getEmployeesWithoutIDs():
    perfect = []
    with open("Employees.txt", 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            expr = r"[\w]+[,]?[\s][\w]+"
            found = re.findall(expr, line)
            name = found[0]
            expr = r"[a-fA-F0-9]{8}[-]?[a-fA-F0-9]{4}[-]?[a-fA-F0-9]{4}[-]?[a-fA-F0-9]{4}[-]?[a-fA-F0-9]{12}"
            found = re.findall(expr, line)
            if found == []:
                expr = r"[ |,|;]{1}[(]?(?P<One>[0-9]{3})[)]?[\s]?[-]?(?P<Two>[0-9]{3})[-]?(?P<Three>[0-9]{4})[ |,|;]{1}"    # REGEX FOR PHONE NUMBER
                found = re.findall(expr, line)
                # If phone number exists
                if found != []:
                    # If it's in <Last>, <First> format
                    if re.search(r",", name):
                        m = re.match(r"(?P<Last>[\w]+), (?P<First>[\w]+)", name)
                        name = m.group("First") + " " + m.group("Last")
                    perfect.append(name)
                expr = r"[\w]+[\s]?[\w]+$"
                found = re.findall(expr, line)
                # If state exists
                if found != []:
                    if re.search(r",", name):
                        m = re.match(r"(?P<Last>[\w]+), (?P<First>[\w]+)", name)
                        name = m.group("First") + " " + m.group("Last")
                    if name not in perfect:
                        perfect.append(name)    
    perfect.sort()

    return perfect

def getEmployeesWithPhones():
    perfect = {}
    with open("Employees.txt", 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            expr = r"[\w]+[,]?[\s][\w]+"
            found = re.findall(expr, line)
            name = found[0]
            expr = r"[ |,|;]{1}[(]?(?P<One>[0-9]{3})[)]?[\s]?[-]?(?P<Two>[0-9]{3})[-]?(?P<Three>[0-9]{4})[ |,|;]{1}"    # REGEX FOR PHONE NUMBER
            found = re.findall(expr, line)
            # If phone number exists
            if found != []:
                # If it's in <Last>, <First> format
                if re.search(r",", name):
                    m = re.match(r"(?P<Last>[\w]+), (?P<First>[\w]+)", name)
                    name = m.group("First") + " " + m.group("Last")
                phonenumber = "(" + found[0][0] + ") " + found[0][1] + "-" + found[0][2]
                perfect[name] = phonenumber

    return perfect

def getEmployeesWithStates():
    perfect = {}
    with open("Employees.txt", 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            expr = r"[\w]+[,]?[\s][\w]+"
            found = re.findall(expr, line)
            name = found[0]
            expr = r"[\w]+[\s]?[\w]+$"          # REGEX FOR STATE
            found = re.findall(expr, line)
            # If state exists
            if found != []:
                # If it's in <Last>, <First> format
                if re.search(r",", name):
                    m = re.match(r"(?P<Last>[\w]+), (?P<First>[\w]+)", name)
                    name = m.group("First") + " " + m.group("Last")
                perfect[name] = found[0]

    return perfect

def getCompleteEntries():
    perfect = {}
    with open("Employees.txt", 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            expr = r"[\w]+[,]?[\s][\w]+"
            found = re.findall(expr, line)
            name = found[0]
            expr = r"[a-fA-F0-9]{8}[-]?[a-fA-F0-9]{4}[-]?[a-fA-F0-9]{4}[-]?[a-fA-F0-9]{4}[-]?[a-fA-F0-9]{12}"   # REGEX FOR ID
            found = re.findall(expr, line)
            # If ID exists
            if found != []:
                i = found[0]
                ID = str(UUID(i))    
                expr = r"[ |,|;]{1}[(]?(?P<One>[0-9]{3})[)]?[\s]?[-]?(?P<Two>[0-9]{3})[-]?(?P<Three>[0-9]{4})[ |,|;]{1}"    # REGEX FOR PHONE NUMBER
                found = re.findall(expr, line)
                # If phone number exists
                if found != []:
                    phonenumber = "(" + found[0][0] + ") " + found[0][1] + "-" + found[0][2]
                    expr = r"[\w]+[\s]?[\w]+$"          # REGEX FOR STATE
                    found = re.findall(expr, line)
                    # If state exists
                    if found != []:
                        state = found[0]
                        # If it's in <Last>, <First> format
                        if re.search(r",", name):
                            m = re.match(r"(?P<Last>[\w]+), (?P<First>[\w]+)", name)
                            name = m.group("First") + " " + m.group("Last")
                        perfect[name] = tuple([ID, phonenumber, state])

    return perfect

if __name__ == "__main__":
    with open("output.txt", 'w') as myFile:
        myFile.write("PART 1\n")
        url = "http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"
        result = getUrlParts(url)
        print("\nThis should be tuple : " + str(type(result)))
        for i in result:
            myFile.write(i)
            myFile.write("   ")
        myFile.write("\n")
        url = "http://www.naver.com/FUCK/YOU?A=69&B=74&C=892&D=58778285"
        result = getUrlParts(url)
        for i in result:
            myFile.write(i)
            myFile.write("   ")
        myFile.write("\n")
        url = "http://www.pornhub.com/SEX/HARDCORE?abcd=sibal&efg=gaesaeki&hij=jotgga"
        result = getUrlParts(url)
        for i in result:
            myFile.write(i)
            myFile.write("   ")
        myFile.write("\n")

        myFile.write("\nPART 2\n")
        url = "http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here"
        result = getQueryParameters(url)
        print("This should be list : " + str(type(result)))
        print("This should be tuple: " + str(type(result[0])))
        for i in result:
            myFile.write(i[0])
            myFile.write("=")
            myFile.write(i[1])
            myFile.write("   ")
        myFile.write("\n")
        url = "http://www.naver.com/FUCK/YOU?A=69&B=74&C=892&D=58778285"
        result = getQueryParameters(url)
        for i in result:
            myFile.write(i[0])
            myFile.write("=")
            myFile.write(i[1])
            myFile.write("   ")
        myFile.write("\n")
        url = "http://www.pornhub.com/SEX/HARDCORE?abcd=sibal&efg=gaesaeki&hij=jotgga"
        result = getQueryParameters(url)
        for i in result:
            myFile.write(i[0])
            myFile.write("=")
            myFile.write(i[1])
            myFile.write("   ")
        myFile.write("\n")

        myFile.write("\nPART 3\n")
        s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
        result = getSpecial(s, "t")
        print("This should be list : " + str(type(result)))
        print("This should be str : " + str(type(result[0])))
        for i in result:
            myFile.write(i)
            myFile.write("   ")
        myFile.write("\n")
        s = "Sit Sat Sas Sos Sis SAK sSsSa SSDWEAR SDKLJ KLJKLDS klJKLFS djswasrs skljnkljg njdj"
        result = getSpecial(s, "s")
        for i in result:
            myFile.write(i)
            myFile.write("   ")
        myFile.write("\n")
        s = "Create a Python file name regexApppy and do all of your work in that file...."
        result = getSpecial(s, "e")
        for i in result:
            myFile.write(i)
            myFile.write("   ")
        myFile.write("\n")

        myFile.write("\nPART 4\n")    
        s = "my mac address is 58:1C:0A:6E:39:4D."
        result = getRealMAC(s)
        print("This should be str : " + str(type(result)))
        myFile.write(result)
        myFile.write("\n")
        s = "mymacaddressis58:1C:0A:6E:39:4D."
        result = getRealMAC(s)
        myFile.write(result)
        myFile.write("\n")
        s = "my mac 58:1C:0A:6E:39:4D address is."
        result = getRealMAC(s)
        myFile.write(result)
        myFile.write("\n")
        s = "58:1c:0a:6E:39:4Dthis is my mac address."
        result = getRealMAC(s)
        myFile.write(result)
        myFile.write("\n")

        myFile.write("\nPART 5\n")
        result = getRejectedEntries()
        print("This should be list : " + str(type(result)))
        for i in result:
            myFile.write(i)
            myFile.write("\n")

        myFile.write("\nPART 6\n")
        result = getEmployeesWithIDs()
        print("This should be dictionary : " + str(type(result)))
        keys = []
        for i in result:
            keys.append(i)
        keys.sort()
        for i in keys:
            myFile.write(i)
            myFile.write(":")
            myFile.write(result[i])
            myFile.write("\n")

        myFile.write("\nPART 7\n")
        result = getEmployeesWithoutIDs()
        print("This should be list : " + str(type(result)))
        for i in result:
            myFile.write(i)
            myFile.write("\n")

        myFile.write("\nPART 8\n")
        result = getEmployeesWithPhones()
        print("This should be dictionary : " + str(type(result)))
        keys = []
        for i in result:
            keys.append(i)
        keys.sort()
        for i in keys:
            myFile.write(i)
            myFile.write(":")
            myFile.write(result[i])
            myFile.write("\n")

        myFile.write("\nPART 9\n")
        result = getEmployeesWithStates()
        print("This should be dictionary : " + str(type(result)))
        keys = []
        for i in result:
            keys.append(i)
        keys.sort()
        for i in keys:
            myFile.write(i)
            myFile.write(":")
            myFile.write(result[i])
            myFile.write("\n")

        myFile.write("\nPART 10\n")
        result = getCompleteEntries()
        print("This should be dictionary : " + str(type(result)))
        print("This should be tuple: " + str(type(result["Ada Houston"])) + "\n")
        keys = []
        for i in result:
            keys.append(i)
        keys.sort()
        for i in keys:
            myFile.write(i)
            myFile.write(":")
            myFile.write("   ")
            myFile.write(result[i][0])
            myFile.write("   ")
            myFile.write(result[i][1])
            myFile.write("   ")
            myFile.write(result[i][2])
            myFile.write("\n")
        myFile.write("\n")
    '''
    print("\nPART 1\n")
    print("getUrlParts")
    url = "http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"
    print(getUrlParts(url))
    print("")
    print("getQueryParameters")
    url = "http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here"
    print(getQueryParameters(url))
    print("")
    print("getSpecial")
    s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
    print(getSpecial(s, "t"))
    print("")
    print("getRealMAC")
    s = "my mac address is 58:1C:0A:6E:39:4D."
    print(getRealMAC(s))
    print("\nPART2\n")
    print("getRejectedEntries")
    print(getRejectedEntries())
    print("")
    print("getEmployeesWithIDs")
    print(getEmployeesWithIDs())
    print("")
    print("getEmployeesWithoutIDs")
    print(getEmployeesWithoutIDs())
    print("")
    print("getEmployeesWithPhones")
    print(getEmployeesWithPhones())
    print("")
    print("getEmployeesWithStates")
    print(getEmployeesWithStates())
    print("")
    print("getCompleteEntries")
    print(getCompleteEntries())
    print("")
    '''
