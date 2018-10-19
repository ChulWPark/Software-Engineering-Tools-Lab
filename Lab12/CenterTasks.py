#! /user/local/bin/python3.4

def getDetails():
    perfect = {}
    with open('community.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        courses = all_lines[1].split()
        courses = courses[2:]
        for line in all_lines[3:]:
            split_line = line.split('|')
            fullname = split_line[0].strip()
            scores = split_line[1:]
            i = 0
            for score in scores:
                score = score.strip()
                if score != '-':
                    if fullname not in perfect:
                        perfect[fullname] = []
                    perfect[fullname].append(tuple([courses[i], float(score)]))
                i = i + 1
    for stuff in perfect:
        perfect[stuff].sort()
    return perfect

def getPerformance():
    perfect = {}
    with open('community.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        courses = all_lines[1].split()
        courses = courses[2:]
        for line in all_lines[3:]:
            split_line = line.split('|')
            fullname = split_line[0].strip()
            scores = split_line[1:]
            i = 0
            for score in scores:
                score = score.strip()
                if score != '-':
                    if courses[i] not in perfect:
                        perfect[courses[i]] = []
                    perfect[courses[i]].append(tuple([fullname, float(score)]))
                i = i + 1
    for stuff in perfect:
        perfect[stuff].sort()
    return perfect

def getHighest(course):
    perfect = getPerformance()
    entry = perfect[course]
    maxi = 0
    for tupelem in entry:
        if tupelem[1] > maxi:
            maxi = tupelem[1]
            save = tupelem
    return save
    
def getMean(course):
    perfect = getPerformance()
    entry = perfect[course]
    accum = 0
    for tupelem in entry:
        accum = accum + tupelem[1]
    mean = round(accum / len(entry), 2)
    return mean
    
def getCumulativeScore(name):
    hourdict = {}
    with open('hours.txt', 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines[2:]:
            line = line.split()
            course = line[0]
            hour = int(line[1])
            hourdict[course] = hour
    perfect = getDetails()
    entry = perfect[name]
    accum = 0
    hrsum = 0
    for tupelem in entry:
        accum = accum + tupelem[1] * hourdict[tupelem[0]]
        hrsum = hrsum + hourdict[tupelem[0]]
    cumscore = round(accum / hrsum, 2)
    return cumscore

if __name__ == "__main__":
    print("\ntesting getDetails()...")
    f1 = getDetails()
    print(f1['Trent Niccum'])
    print(f1['Sadie Farkas'])
    print("\ntesting getPerformance()...")
    f2 = getPerformance()
    print(f2['MET136'])
    print(len(f2['MET136']))
    print(f2['MET139'])
    print(len(f2['MET139']))
    print("\ntesting getHighest(course)...")
    print(getHighest('MET290'))
    print(getHighest('MET388'))
    print("\ntesting getMean(course)...")
    print(getMean('MET475'))
    print(getMean('MET344'))
    print("\ntesting getCumulativeScore(name)...")
    print(getCumulativeScore('Floria Uribe'))
    print(getCumulativeScore('Melba Gist'))
    print("")
