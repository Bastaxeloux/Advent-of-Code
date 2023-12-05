# Description: Advent of Code - Day 1

# Part 1
with open("input.txt", "r") as file:
    somme = []
    for line in file.readlines():
        calibrationvalues = []
        l = len(line)
        for i in range(l):
            if line[i].isnumeric():
                calibrationvalues.append(int(line[i]))
        somme.append(calibrationvalues[0]*10 + calibrationvalues[len(calibrationvalues)-1])
        print(line, calibrationvalues)
    total = sum(somme)
    print("Total: ", total)
        #print(line)
        #print(l)

# Part 2

nombres = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
           "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

with open("input.txt", "r") as file:
    somme = []
    for line in file.readlines():
        calibrationvalues = []
        cal2 = []
        l = len(line)
        trouve1 = False
        trouve2 = False
        for i in range(l):
            j=l-i-1
            pre = line[:i]
            suf = line[j:]
            for c in nombres:
                if c in pre and trouve1 == False:
                    calibrationvalues.append(nombres[c])
                    trouve1 = True
                if c in suf and trouve2 == False:
                    cal2.append(nombres[c])
                    trouve2 = True
            if line[i].isnumeric():
                calibrationvalues.append(int(line[i]))
            if line[j].isnumeric():
                cal2.append(int(line[j]))
        if len(cal2) > 0:
            calibrationvalues.append(cal2[0])
        print(line, calibrationvalues)
        somme.append(calibrationvalues[0]*10 + calibrationvalues[len(calibrationvalues)-1])
    total = sum(somme)
    print("Total: ", total)