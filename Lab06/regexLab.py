#! /user/local/bin/python3.4

import re

def extractValues(sentence):
    expr = r"[-|+]?[\d]+[.]?[\d]+[e|E]?[-|+]?[\d]*"
    perfect = re.findall(expr, sentence)
    
    return perfect

def getSwitches(commandline):
    perfect = []
    expr = r"[\\|+]{1}([\w]{1}[\s]+[\w/]*)"
    switches = re.findall(expr, commandline)
    for switch in switches:
        key = switch[0]
        expr = r"[\w/]+"
        search = re.search(expr, switch[1:])
        if search != None:
            perfect.append(tuple([key, search.group(0)]))
    perfect.sort()

    return perfect

if __name__ == "__main__":
    s = "With the electron's charge being -1.6022e-19, some choices you have are -110, -32.0 and +55. Assume that pi equals 3.1415, 'e' equals 2.7 and Na is +6.0221E+023."
    print(extractValues(s))
    print(getSwitches("myScript.bash +v  \i 2   +p  /local/bin/somefolder"))
