#! /user/local/bin/python3.4
import os

# TASK 1
def getComponentCountByProject(projectID):
    # Read File
    valid = False
    Rcount = 0
    Lcount = 0
    Ccount = 0
    Tcount = 0
    Rlist = []
    Llist = []
    Clist = []
    Tlist = []
    with open('projects.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            if line != all_lines[0] and line != all_lines[1]:
                split_line = line.split()
                if split_line[1] == projectID:
                    valid = True
                    targetPath = "Circuits/circuit_" + split_line[0] + ".txt"
                    with open(targetPath, 'r') as myFile2:
                        five_lines = myFile2.readlines()
                        all_components = five_lines[4].split(", ")
                        for component in all_components:
                            if component[0] == "R":
                                if component not in Rlist:
                                    Rlist.append(component)
                            elif component[0] == "L":
                                if component not in Llist:
                                    Llist.append(component)
                            elif component[0] == "C":
                                if component not in Clist:
                                    Clist.append(component)
                            elif component[0] == "T":
                                if component not in Tlist:
                                    Tlist.append(component)
    Rcount = len(Rlist)
    Lcount = len(Llist)
    Ccount = len(Clist)
    Tcount = len(Tlist)

    # EDGE CASES
    if valid == False:
        return None

    perfect = tuple([Rcount, Lcount, Ccount, Tcount])

    return perfect

# TASK 2
def getComponentCountByStudent(studentName):
    perfect = tuple([])
    Rcount = 0
    Lcount = 0
    Ccount = 0
    Tcount = 0
    Rlist = []
    Llist = []
    Clist = []
    Tlist = []
    name_valid = False
    participation_valid = False
    with open('students.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            if line != all_lines[0] and line != all_lines[1]:
                split_line = line.split("|")
                trim_name = split_line[0].strip()
                if trim_name == studentName:
                    target = split_line[1].replace(" ", "")
                    target = target.replace("\n", "")
                    name_valid = True
                    for noneed1, noneed2, circuitFiles in os.walk("Circuits"):
                        for circuitFile in circuitFiles:
                            circuitFile = "Circuits/" + str(circuitFile)
                            with open(circuitFile, 'r') as myFile2:
                                five_lines = myFile2.readlines()
                                all_students = five_lines[1].split(", ")
                                for student in all_students:
                                    student = student.replace("\n", "")
                                    if student == target:
                                        participation_valid = True
                                        all_components = five_lines[4].split(", ")
                                        for component in all_components:
                                            if component[0] == "R":
                                                if component not in Rlist:
                                                    Rlist.append(component)
                                            elif component[0] == "L":
                                                if component not in Llist:
                                                    Llist.append(component)
                                            elif component[0] == "C":
                                                if component not in Clist:
                                                    Clist.append(component)
                                            elif component[0] == "T":
                                                if component not in Tlist:
                                                    Tlist.append(component)
    Rcount = len(Rlist)
    Lcount = len(Llist)
    Ccount = len(Clist)
    Tcount = len(Tlist)

    # EDGE CASES
    if name_valid == False:
        return None
    elif participation_valid == False:
        return tuple([])

    perfect = tuple([Rcount, Lcount, Ccount, Tcount])

    return perfect

# TASK 3
def getParticipationByStudent(studentName):
    participation_list = []
    projectID_list = []
    participation_valid = False
    name_valid = False
    with open('students.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            if line != all_lines[0] and line != all_lines[1]:
                split_line = line.split("|")
                trim_name = split_line[0].strip()
                if trim_name == studentName:
                    name_valid = True
                    target = split_line[1].strip()
                    for noneed1, noneed2, circuitFiles in os.walk("Circuits"):
                        for circuitFile in circuitFiles:
                            circuitFile = "Circuits/" + str(circuitFile)
                            with open(circuitFile, 'r') as myFile2:
                                five_lines = myFile2.readlines()
                                five_lines[1] = five_lines[1].replace("\n", "")
                                all_students = five_lines[1].split(", ")
                                if target in all_students:
                                    participation_valid = True
                                    participation_list.append(circuitFile[17:22])
                    with open('projects.txt', 'r') as myFile3:
                        all_lines = myFile3.readlines()
                        for line in all_lines:
                            if line != all_lines[0] and line != all_lines[1]:
                                split_line = line.split()
                                if split_line[0] in participation_list:
                                    projectID_list.append(split_line[1])

    perfect = set(projectID_list)

    # EDGE CASES
    if name_valid == False:
        return None
    elif participation_valid == False:
        return set([])

    return perfect

# TASK 4
def getParticipationByProject(projectID):
    participation_list = []
    name_list = []
    ID_valid = False
    with open('projects.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            if line != all_lines[0] and line != all_lines[1]:
                split_line = line.split()
                if split_line[1] == projectID:
                    ID_valid = True
                    targetPath = "Circuits/circuit_" + split_line[0] + ".txt"
                    with open(targetPath, 'r') as myFile2:
                        five_lines = myFile2.readlines()
                        students = five_lines[1].split(", ")
                        for student in students:
                            student = student.replace("\n", "")
                            participation_list.append(student)

    with open('students.txt', 'r') as myFile3:
        all_lines = myFile3.readlines()
        for line in all_lines:
            if line != all_lines[0] and line != all_lines[1]:
                split_line = line.split("|")
                target = split_line[1].strip()
                if target in participation_list:
                    name_list.append(split_line[0].strip())

    perfect = set(name_list)

    # EDGE CASES
    if ID_valid == False:
        return None

    return perfect

# TASK 5
def getProjectByComponent(components):
    projectID_list = []
    circuit_list = []
    perfect = {}
    for component in components:
        for noneed1, noneed2, circuitFiles in os.walk("Circuits"):
            for circuitFile in circuitFiles:
                circuitFile = "Circuits/" + str(circuitFile)
                with open(circuitFile, 'r') as myFile2:
                    five_lines = myFile2.readlines()
                    all_components = five_lines[4].split(", ")
                    if component in all_components:
                        circuit_list.append(circuitFile[17:22])
        with open('projects.txt', 'r') as myFile3:
            all_lines = myFile3.readlines()
            for line in all_lines:
                if line != all_lines[0] and line != all_lines[1]:
                    split_line = line.split()
                    if split_line[0] in circuit_list:
                        projectID_list.append(split_line[1])
        perfect[component] = set(projectID_list)
        circuit_list = []
        projectID_list = []

    return perfect

# TASK 6
def getStudentByComponent(components):
    perfect = {}
    participation_list = []
    name_list = []
    for component in components:
        for noneed1, noneed2, circuitFiles in os.walk("Circuits"):
            for circuitFile in circuitFiles:
                circuitFile = "Circuits/" + str(circuitFile)
                with open(circuitFile, 'r') as myFile:
                    five_lines = myFile.readlines()
                    all_components = five_lines[4].split(", ")
                    if component in all_components:
                        all_students = five_lines[1].split(", ")
                        for student in all_students:
                            student = student.replace("\n", "")
                            participation_list.append(student)
        with open('students.txt', 'r') as myFile2:
            all_lines = myFile2.readlines()
            for line in all_lines:
                if line != all_lines[0] and line != all_lines[1]:
                    split_line = line.split("|")
                    target = split_line[1].strip()
                    if target in participation_list:
                        name_list.append(split_line[0].strip())
        perfect[component] = set(name_list)
        name_list = []
        participation_list = []

    return perfect


# TASK 7
def getComponentByStudent(studentNames):
    name_valid = False
    perfect = {}
    component_list = []
    for student in studentNames:
        with open('students.txt', 'r') as myFile:
            all_lines = myFile.readlines()
            for line in all_lines:
                split_line = line.split("|")
                target = split_line[0].strip()
                if target == student:
                    name_valid = True
                    target = split_line[1].strip()
                    for noneed1, noneed2, circuitFiles in os.walk("Circuits"):
                        for circuitFile in circuitFiles:
                            circuitFile = "Circuits/" + str(circuitFile)
                            with open(circuitFile, 'r') as myFile2:
                                five_lines = myFile2.readlines()
                                five_lines[1] = five_lines[1].replace("\n", "")
                                all_participants = five_lines[1].split(", ")
                                if target in all_participants:
                                    five_lines[2] = five_lines[4].replace("\n", "")
                                    all_components = five_lines[4].split(", ")
                                    for component in all_components:
                                        component_list.append(component)
        perfect[student] = set(component_list)
        component_list = []
    
    if name_valid == False:
        return None
    return perfect


# TASK 8
def getCommonByProject(projectID1, projectID2):
    circuit_list1 = []
    circuit_list2 = []
    component_list1 = []
    component_list2 = []
    perfect = []
    with open('projects.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            if line != all_lines[0] and line != all_lines[1]:
                split_line = line.split()
                if split_line[1] == projectID1:
                    circuit_list1.append(split_line[0])
                if split_line[1] == projectID2:
                    circuit_list2.append(split_line[0])
    # EDGE CASE
    if circuit_list1 == [] or circuit_list2 == []:
        return None
    for circuit in circuit_list1:
        targetPath = "Circuits/circuit_" + circuit + ".txt"
        with open(targetPath, 'r') as myFile2:
            five_lines = myFile2.readlines()
            all_components = five_lines[4].split(", ")
            for component in all_components:
                if component not in component_list1:
                    component_list1.append(component)
    for circuit in circuit_list2:
        targetPath = "Circuits/circuit_" + circuit + ".txt"
        with open(targetPath, 'r') as myFile3:
            five_lines = myFile3.readlines()
            all_components = five_lines[4].split(", ")
            for component in all_components:
                if component not in component_list2:
                    component_list2.append(component)
    for component in component_list1:
        if component in component_list2:
            perfect.append(component)
    perfect.sort()

    return perfect

# TASK 9
def getCommonByStudent(studentName1, studentName2):
    perfect = []
    temp1 = [studentName1]
    temp2 = [studentName2]
    param1 = set(temp1)
    param2 = set(temp2)
    dictionary1 = getComponentByStudent(param1)
    dictionary2 = getComponentByStudent(param2)
    if dictionary1 == None or dictionary2 == None:
        return None
    component_set1 = dictionary1[studentName1]
    component_set2 = dictionary2[studentName2]
    for component in component_set1:
        if component in component_set2:
            perfect.append(component)
    perfect.sort()

    return perfect

# TASK 10
def getProjectByCircuit():
    perfect = {}
    circuit_list = []
    ID_list = []
    trash_list = []
    with open('projects.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            if line != all_lines[0] and line != all_lines[1]:
                split_line = line.split()
                circuit_list.append(split_line[0])
    for circuit in circuit_list:
        if circuit not in trash_list:
            for line in all_lines:
                if line != all_lines[0] and line != all_lines[1]:
                    split_line = line.split()
                    if split_line[0] == circuit:
                        ID_list.append(split_line[1])
            ID_list.sort()
            perfect[circuit] = ID_list
            ID_list = []
            trash_list.append(circuit)

    return perfect

# TASK 11
def getCircuitByStudent():
    perfect = {}
    circuit_list = []
    with open('students.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            if line != all_lines[0] and line != all_lines[1]:
                split_line = line.split("|")
                target = split_line[1].strip()
                for noneed1, noneed2, circuitFiles in os.walk("Circuits"):
                    for circuitFile in circuitFiles:
                        circuitFile = "Circuits/" + str(circuitFile)
                        with open(circuitFile, 'r') as myFile2:
                            five_lines = myFile2.readlines()
                            five_lines[1] = five_lines[1].replace("\n", "")
                            all_participants = five_lines[1].split(", ")
                            if target in all_participants:
                                circuit_list.append(circuitFile[17:22])
                circuit_list.sort()
                perfect[split_line[0].strip()] = circuit_list
                circuit_list = []

    return perfect

# TASK 12
def getCircuitByStudentPartial(studentName):
    perfect = {}
    circuit_list = []
    name_valid = False
    with open('students.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            if line != all_lines[0] and line != all_lines[1]:
                split_line = line.split("|")
                name = split_line[0].strip()
                split_name = name.split(", ")
                if split_name[0] == studentName or split_name[1] == studentName:
                    name_valid = True
                    target = split_line[1].strip()
                    for noneed1, noneed2, circuitFiles in os.walk("Circuits"):
                        for circuitFile in circuitFiles:
                            circuitFile = "Circuits/" + str(circuitFile)
                            with open(circuitFile, 'r') as myFile2:
                                five_lines = myFile2.readlines()
                                five_lines[1] = five_lines[1].replace("\n", "")
                                all_participants = five_lines[1].split(", ")
                                if target in all_participants:
                                    circuit_list.append(circuitFile[17:22])
                    circuit_list.sort()
                    perfect[name] = circuit_list
                    circuit_list = []
    # EDGE CASE
    if name_valid == False:
        return None

    return perfect

'''
if __name__ == "__main__":
    print("EDGE CASE TESTING...")
    print("TASK 1: projectID doesn't exist, return None")
    print(getComponentCountByProject("wrongprojectID"))
    print("TASK 2: student name passed does not exist, return None")
    print(getComponentCountByStudent("wrongname"))
    print("TASK 3: student name passed does not exist, return None")
    print(getParticipationByStudent("wrongname"))
    print("TASK 4: projectID doesn't exist, return None")
    print(getParticipationByProject("wrongprojectID"))
    print("TASK 8: projectID doesn't exist, return None")
    print(getCommonByProject("wrongprojectID", "wrongprojectID"))
    print("TASK 9: student name passed does not exist, return None")
    print(getCommonByStudent("wrongname", "wrongname"))
    print("TASK 12: student name passed does not exist, return None")
    print(getCircuitByStudentPartial("wrongname"))
    
    with open('output.txt', 'w') as myFile:
        myFile.write("TASK 1\n")
        output = getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6")
        for i in output:
            myFile.write(str(i) + " ")
        myFile.write("\n")
        output = getComponentCountByProject("FE647EE2-2EBD-4837-83F0-256C377365FE")
        for i in output:
            myFile.write(str(i) + " ")
        myFile.write("\n")
        output = getComponentCountByProject("90BE0D09-1438-414A-A38B-8309A49C02EF")
        for i in output:
            myFile.write(str(i) + " ")
        myFile.write("\n")

        myFile.write("\nTASK 2\n")
        output = getComponentCountByStudent("Adams, Keith")
        for i in output:
            myFile.write(str(i) + " ")
        myFile.write("\n")
        output = getComponentCountByStudent("Alexander, Carlos")
        for i in output:
            myFile.write(str(i) + " ")
        myFile.write("\n")
        output = getComponentCountByStudent("Allen, Amanda")
        for i in output:
            myFile.write(str(i) + " ")
        myFile.write("\n")
        output = getComponentCountByStudent("Anderson, Debra")
        for i in output:
            myFile.write(str(i) + " ")
        myFile.write("\n")
        output = getComponentCountByStudent("Bailey, Catherine")
        for i in output:
            myFile.write(str(i) + " ")
        myFile.write("\n")

        myFile.write("\nTASK 3\n")
        output = getParticipationByStudent("Adams, Keith")
        output = list(output)
        output.sort()
        for i in output:
            myFile.write(i + " ")
        myFile.write("\n")
        output = getParticipationByStudent("Alexander, Carlos")
        output = list(output)
        output.sort()
        for i in output:
            myFile.write(i + " ")
        myFile.write("\n")
        output = getParticipationByStudent("Allen, Amanda")
        output = list(output)
        output.sort()
        for i in output:
            myFile.write(i + " ")
        myFile.write("\n")
        output = getParticipationByStudent("Anderson, Debra")
        output = list(output)
        output.sort()
        for i in output:
            myFile.write(i + " ")
        myFile.write("\n")
        output = getParticipationByStudent("Bailey, Catherine")
        output = list(output)
        output.sort()
        for i in output:
            myFile.write(i + " ")
        myFile.write("\n")
        myFile.write("\n")

        myFile.write("TASK 4\n")
        output = getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6")
        output = list(output)
        output.sort()
        for i in output:
            myFile.write(i + " ")
        myFile.write("\n")
        output = getParticipationByProject("FE647EE2-2EBD-4837-83F0-256C377365FE")
        output = list(output)
        output.sort()
        for i in output:
            myFile.write(i + " ")
        myFile.write("\n")
        output = getParticipationByProject("90BE0D09-1438-414A-A38B-8309A49C02EF")
        output = list(output)
        output.sort()
        for i in output:
            myFile.write(i + " ")
        myFile.write("\n")

        myFile.write("\nTASK 5\n")
        param = {"T71.386", "T20.187"}
        output = getProjectByComponent(param)
        param = list(param)
        param.sort()
        for i in param:
            temp = output[i]
            temp = list(temp)
            temp.sort()
            myFile.write(i + "\n")
            for j in temp:
                myFile.write(j + " ")
            myFile.write("\n")

        myFile.write("\nTASK 6\n")
        param = {"T71.386", "T20.187"}
        output = getStudentByComponent(param)
        param = list(param)
        param.sort()
        for i in param:
            temp = output[i]
            temp = list(temp)
            temp.sort()
            myFile.write(i + "\n")
            for j in temp:
                myFile.write(j + " ")
            myFile.write("\n")

        myFile.write("\nTASK 7\n")
        param = {"Adams, Keith", "Alexander, Carlos", "Allen, Amanda", "Anderson, Debra", "Bailey, Catherine"}
        output = getComponentByStudent(param)
        param = list(param)
        param.sort()
        for i in param:
            temp = output[i]
            temp = list(temp)
            temp.sort()
            myFile.write(i + "\n")
            for j in temp:
                myFile.write(j + " ")
            myFile.write("\n")

        myFile.write("\nTASK 8\n")
        output = getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "FE647EE2-2EBD-4837-83F0-256C377365FE")
        for i in output:
            myFile.write(i + " ")
        myFile.write("\n")

        myFile.write("\nTASK 9\n")
        output = getCommonByStudent("Adams, Keith", "James, Randy")
        for i in output:
            myFile.write(i + " ")
        myFile.write("\n")
        output = getCommonByStudent("Adams, Keith", "Alexander, Carlos")
        for i in output:
            myFile.write(i + " ")
        myFile.write("\n")
        output = getCommonByStudent("Allen, Amanda", "Anderson, Debra")
        for i in output:
            myFile.write(i + " ")
        myFile.write("\n")

        myFile.write("\nTASK 10\n")
        output = getProjectByCircuit()
        circuit_list = []
        with open('projects.txt', 'r') as pFile:
            all_lines = pFile.readlines()
            for line in all_lines:
                if line != all_lines[0] and line != all_lines[1]:
                    split_line = line.split()
                    circuit_list.append(split_line[0])
            for i in circuit_list:
                temp = output[i]
                temp = list(temp)
                temp.sort()
                myFile.write(i + "\n")
                for j in temp:
                    myFile.write(j + " ")
                    myFile.write("\n")

        myFile.write("\nTASK 11\n")
        output = getCircuitByStudent()
        student_list = []
        with open('students.txt', 'r') as sFile:
            all_lines = sFile.readlines()
            for line in all_lines:
                if line != all_lines[0] and line != all_lines[1]:
                    split_line = line.split("|")
                    fullname = split_line[0].strip()
                    student_list.append(fullname)
            for i in student_list:
                temp = output[i]
                temp = list(temp)
                myFile.write(i + "\n")
                for j in temp:
                    myFile.write(j + " ")
                    myFile.write("\n")

        myFile.write("\nTASK 12\n")
        param = "James"
        output = getCircuitByStudentPartial(param)
        student_list = []
        with open('students.txt', 'r') as sFile:
            all_lines = sFile.readlines()
            for line in all_lines:
                if line != all_lines[0] and line != all_lines[1]:
                    split_line = line.split("|")
                    fullname = split_line[0].strip()
                    lastname, firstname = fullname.split(", ")
                    if lastname == param or firstname == param:
                        student_list.append(fullname)
            for i in student_list:
                temp = output[i]
                temp = list(temp)
                myFile.write(i + "\n")
                for j in temp:
                    myFile.write(j + " ")
                    myFile.write("\n") '''
