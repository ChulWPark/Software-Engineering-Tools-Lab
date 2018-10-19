#! /user/local/bin/python3.4

import re
import random
import operator
from enum import Enum

class Level(Enum):
    freshman = "Freshman"
    sophomore = "Sophomore"
    junior = "Junior"
    senior = "Senior"

class Student:
    # Initializer
    def __init__(self, ID, firstName, lastName, level):
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        if not isinstance(level, Level):
            raise TypeError("The argument must be an instance of the 'Level' Enum.")
        else:
            self.level = level
    # String Representation
    def __str__(self):
        rep = self.ID + ", " + self.firstName + " " + self.lastName + ", " + self.level.value
        return rep

class Circuit:
    # Initializer
    def __init__(self, ID, resistors, capacitors, inductors, transistors):
        self.ID = ID
        # Validity Check for resistor list
        for resistor in resistors:
            expr = r"(?P<type>[\w]{1})[0-9]+[.][0-9]+"
            m = re.match(expr, resistor)
            if m.group("type") != "R":
                raise ValueError("The resistors' list contain invalid components.")
        self.resistors = resistors
        # Validity Check for capacitor list
        for capacitor in capacitors:
            expr = r"(?P<type>[\w]{1})[0-9]+[.][0-9]+"
            m = re.match(expr, capacitor)
            if m.group("type") != "C":
                raise ValueError("The capacitors' list contain invalid components.")
        self.capacitors = capacitors
        # Validity Check for inductor list
        for inductor in inductors:
            expr = r"(?P<type>[\w]{1})[0-9]+[.][0-9]+"
            m = re.match(expr, inductor)
            if m.group("type") != "L":
                raise ValueError("The inductors' list contain invalid components.")
        self.inductors = inductors
        # Validity Check for transistor list
        for transistor in transistors:
            expr = r"(?P<type>[\w]{1})[0-9]+[.][0-9]+"
            m = re.match(expr, transistor)
            if m.group("type") != "T":
                raise ValueError("The transistors' list contain invalid components.")
        self.transistors = transistors
    # String Representation
    def __str__(self):
        rep = self.ID + ": (R = " + str(len(self.resistors)).zfill(2) + ", C = " + str(len(self.capacitors)).zfill(2) + ", L = " + str(len(self.inductors)).zfill(2) + ", T = " + str(len(self.transistors)).zfill(2) + ")"
        return rep
    # getDetails
    def getDetails(self):
        # Sort all component list
        self.resistors.sort()
        self.capacitors.sort()
        self.inductors.sort()
        self.transistors.sort()
        rep = self.ID + ": "
        for resistor in self.resistors:
            rep = rep + str(resistor) + ", "
        for capacitor in self.capacitors:
            rep = rep + str(capacitor) + ", "
        for inductor in self.inductors:
            rep = rep + str(inductor) + ", "
        for transistor in self.transistors:
            rep = rep + str(transistor) + ", "
        rep = rep[0:len(rep) - 2]
        return rep
    # Operator Overload: component in Circuit
    def __contains__(self, component):
        # Check if the component in question is a string
        if not isinstance(component, str):
            raise TypeError("component is not a string.")
        # Check if the component is one of the known types
        expr = r"(?P<type>[\w]{1})[0-9]+[.][0-9]+"
        m = re.match(expr, component)
        if m.group("type") != "R" and m.group("type") != "L" and m.group("type") != "C" and m.group("type") != "T":
            raise ValueError("component is not one of the known types")
        # Check if the component is in the Circuit
        if m.group("type") == "R":
            return component in self.resistors
        if m.group("type") == "C":
            return component in self.capacitors
        if m.group("type") == "L":
            return component in self.inductors
        if m.group("type") == "T":
            return component in self.transistors
    # Operator Overload: Circuit + component / Circuit1 + Circuit2
    def __add__(self, other):
        # Circuit + component
        if isinstance(other, str): 
            expr = r"(?P<type>[\w]{1})[0-9]+[.][0-9]+"
            m = re.match(expr, other)
            # Check if the component is one of the known types
            if m.group("type") != "R" and m.group("type") != "L" and m.group("type") != "C" and m.group("type") != "T":
                raise ValueError("component is not one of the known types")
            if m.group("type") == "R" and other not in self.resistors:
                self.resistors.append(other)
            if m.group("type") == "C" and other not in self.capacitors:
                self.capacitors.append(other)
            if m.group("type") == "L" and other not in self.inductors:
                self.inductors.append(other)
            if m.group("type") == "T" and other not in self.transistors:
                self.transistors.append(other)
            return self
        # Circuit1 + Circuit2
        elif isinstance(other, Circuit):
            newID = random.sample(range(10000, 100000), 1)
            newRlist = []
            newLlist = []
            newClist = []
            newTlist = []
            # newRlist
            for resistor in self.resistors:
                if resistor not in newRlist:
                    newRlist.append(resistor)
            for resistor in other.resistors:
                if resistor not in newRlist:
                    newRlist.append(resistor)
            # newClist
            for capacitor in self.capacitors:
                if capacitor not in newClist:
                    newClist.append(capacitor)
            for capacitor in other.capacitors:
                if capacitor not in newClist:
                    newClist.append(capacitor)
            # newLlist
            for inductor in self.inductors:
                if inductor not in newLlist:
                    newLlist.append(inductor)
            for inductor in other.inductors:
                if inductor not in newLlist:
                    newLlist.append(inductor)
            # newTlist
            for transistor in self.transistors:
                if transistor not in newTlist:
                    newTlist.append(transistor)
            for transistor in other.transistors:
                if transistor not in newTlist:
                    newTlist.append(transistor)
            return Circuit(str(newID[0]), newRlist, newClist, newLlist, newTlist)
        else:
            raise TypeError("+: type is not a string or Circuit class")                
    # Operator Overload: component + Circuit
    def __radd__(self, other):
        return self.__add__(other)
    # Operator Overload: Circuit - component
    def __sub__(self, other):
        if isinstance(other, str):
            expr = r"(?P<type>[\w]{1})[0-9]+[.][0-9]+"
            m = re.match(expr, other)
            # Check if the component is one of the known types
            if m.group("type") != "R" and m.group("type") != "L" and m.group("type") != "C" and m.group("type") != "T":
                raise ValueError("component is not one of the known types")
            if m.group("type") == "R" and other in self.resistors:
                self.resistors.remove(other)
            if m.group("type") == "C" and other in self.capacitors:
                self.capacitors.remove(other)
            if m.group("type") == "L" and other in self.inductors:
                self.inductors.remove(other)
            if m.group("type") == "T" and other in self.transistors:
                self.transistors.remove(other)
            return self
        else:
            raise TypeError("-: type is not a string")

class Project:
    # Initializer
    def __init__(self, ID, participants, circuits):
        self.ID = ID
        # Validate that each of the lists passed is not empty
        if participants == []:
            raise ValueError("participants list is empty")
        for participant in participants:
            if not isinstance(participant, Student):
                raise ValueError("participants list has an element that is not Student class")
        self.participants = participants
        if circuits == []:
            raise ValueError("circuits list is empty")
        for circuit in circuits:
            if not isinstance(circuit, Circuit):
                raise ValueError("circuits list has an element that is not Circuit class")
        self.circuits = circuits
    # String Representation
    def __str__(self):
        rep = self.ID + ": " + str(len(self.circuits)).zfill(2) + " Circuits, " + str(len(self.participants)).zfill(2) + " Participants"
        return rep
    # getDetails
    def getDetails(self):
        multistr = self.ID + "\n\nParticipants:\n"
        self.participants.sort(key=operator.attrgetter("ID"))
        for participant in self.participants:
            multistr = multistr + str(participant) + "\n"
        multistr = multistr + "\nCircuits:\n"
        self.circuits.sort(key=operator.attrgetter("ID"))
        for circuit in self.circuits:
            multistr = multistr + circuit.getDetails() + "\n"
        multistr = multistr[0:len(multistr)-1]
        return multistr
    # Operator Overload: component in Project / Circuit in Project / Student in Project
    def __contains__(self, other):
        # component in Project
        if isinstance(other, str):
            expr = r"(?P<type>[\w]{1})[0-9]+[.][0-9]+"
            m = re.match(expr, other)
            # Check if the component is one of the known types
            if m.group("type") != "R" and m.group("type") != "L" and m.group("type") != "C" and m.group("type") != "T":
                raise ValueError("component is not one of the known types")
            for circuit in self.circuits:
                if other in circuit.resistors or other in circuit.capacitors or other in circuit.inductors or other in circuit.transistors:
                    return True
            return False
        # Circuit in Project
        elif isinstance(other, Circuit):
            for circuit in self.circuits:
                if other.ID == circuit.ID:
                    return True
            return False
        # Student in Project
        elif isinstance(other, Student):
            for participant in self.participants:
                if other.ID == participant.ID:
                    return True
            return False
        # TypeError
        else:
            raise TypeError("in: type should be string or Circuit or Student")
    # Operator Overload: Project + Circuit / Project + Student
    def __add__(self, other):
        # Project + Circuit
        if isinstance(other, Circuit):
            for circuit in self.circuits:
                if other.ID == circuit.ID:
                    return self
            self.circuits.append(other)
            return self
        # Project + Student
        elif isinstance(other, Student):
            for participant in self.participants:
                if other.ID == participant.ID:
                    return self
            self.participants.append(other)
            return self
        else:
            raise TypeError("+: type should be Circuit or Student")
    # Operator Overload: Project - Circuit / Project - Student
    def __sub__(self, other):
        # Project - Circuit
        if isinstance(other, Circuit):
            if other in self.circuits:
                self.circuits.remove(other)
            return self
        # Project - Student
        elif isinstance(other, Student):
            if other in self.participants:
                self.participants.remove(other)
            return self
        else:
            raise TypeError("-: type should be Circuit or Student")

class Capstone(Project):
    # Initializer
    def __init__(self, ID, participants, circuits):
        Project.__init__(self, ID, participants, circuits)
        for participant in self.participants:
            if participant.level != Level.senior:
                raise ValueError("All participating students should be seniors")
    # Member Override: Project + Student
    def __add__(self, other):
        if isinstance(other, Student):
            if other.level != Level.senior:
                raise ValueError("Participating student should be a senior")
        Project.__add__(self, other)
        return self

# Conditional Main Block
if __name__ == "__main__":
    print("-----------------------------------------------------------------------------------------------------------------")
    student1 = Student("00123-45678", "Chul Woo", "Park", Level.junior)
    print("str(Student) testing...")
    print(str(student1))
    circuit1 = Circuit("99887", ["R436.943", "R206.298"], ["C261.054", "C668.027", "C194.315"], ["L49.234"], ["T663.350"])
    print("-----------------------------------------------------------------------------------------------------------------")
    print("str(Circuit) testing...")
    print(str(circuit1))
    print("-----------------------------------------------------------------------------------------------------------------")
    print("getDetails(self) testing...")
    print(circuit1.getDetails())
    print("-----------------------------------------------------------------------------------------------------------------")
    print("__contains__ testing...")
    if "C261.054" in circuit1:
        print("C261.054 is in the circuit1!")
    else:
        print("BAD")
    if "R436.943" in circuit1:
        print("R436.943 is in the circuit1!")
    else:
        print("BAD")
    if "T123.456" in circuit1:
        print("BAD")
    else:
        print("T123.456 is not in the circuit1")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Circuit + component testing...")
    perfect = circuit1 + "T123.456"
    print(circuit1.getDetails())
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Circuit1 + Circuit2 testing...")
    circuit2 = Circuit("12345", ["R123.456"], ["C123.456", "C789.101"], ["L123.456"], ["T789.101"])
    perfect = circuit1 + circuit2
    print(perfect.getDetails())
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Circuit - component testing...")
    perfect = perfect - "R123.456"
    print(perfect.getDetails())
    print("-----------------------------------------------------------------------------------------------------------------")
    student1 = Student("00123-45678", "Chul Woo", "Park", Level.junior)
    student2 = Student("00095-11160", "Eun Chae", "Lee", Level.junior)
    student3 = Student("00321-87654", "Sang Hun", "Kim", Level.senior)
    student4 = Student("00111-22334", "Jeong Min", "Kim", Level.senior)
    project1 = Project("38753067-e3a8-4c9e-bbde-cd13165fa21e", [student1, student2, student3, student4], [circuit1, circuit2])
    print("str(Project) testing...")
    print(str(project1))
    print("-----------------------------------------------------------------------------------------------------------------")
    print("getDetails(self) testing...")
    print(project1.getDetails())
    print("-----------------------------------------------------------------------------------------------------------------")
    print("component in Project testing...")
    if "R123.456" in project1:
        print("R123.456 is in project1")
    else:
        print("BAD")
    if "R999.999" in project1:
        print("BAD")
    else:
        print("R999.999 is not in project1")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Circuit in Project testing...")
    if circuit1 in project1:
        print("circuit1 is in project1")
    else:
        print("BAD")
    if perfect in project1:
        print("BAD")
    else:
        print("perfect is not in project1")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Student in Project testing...")
    if student1 in project1:
        print("student1 is in project1")
    else:
        print("BAD")
    student5 = Student("99999-99999", "Wrong", "Name", Level.freshman)
    if student5 in project1:
        print("BAD")
    else:
        print("student5 is not in project1")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Project + Circuit testing...")
    circuit3 = Circuit("99999", ["R111.111", "R222.222"], ["C555.555", "C666.666"], ["L154.321"], ["T494.383", "T513.521"])
    project1 = project1 + circuit3
    print(project1.getDetails())
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Project + Student testing...")
    student5 = Student("10293-84756", "Sibal", "Jotgga", Level.sophomore)
    project1 = project1 + student5
    print(project1.getDetails())
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Project - Circuit testing...")
    project1 = project1 - circuit3
    print(project1.getDetails())
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Project - Student testing...")
    project1 = project1 - student5
    print(project1.getDetails())
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Capstone __init__ testing...")
    capstone1 = Capstone("38753067-e3a8-4c9e-bbde-cd13165fa21e", [student3, student4], [circuit1, circuit2])
    print(capstone1.getDetails())
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Capstone __add__ testing...")
    student6 = Student("98421-47021", "Sex", "Machine", Level.senior)
    capstone1 = capstone1 + student6
    print(capstone1.getDetails())
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Capstone __sub__testing...")
    capstone1 = capstone1 - student6
    print(capstone1.getDetails())
    print("-----------------------------------------------------------------------------------------------------------------")
