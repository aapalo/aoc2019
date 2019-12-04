#!/usr/bin/python3

import time

'''     #######     '''

date = 3
dev = 0 # extra prints
part = 3 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def coordToSet(instructions):
    a = set()
    x = 0
    y = 0
    a.add((y,x))
    for i in instructions:
        dir = i[0]
        steps = int(i[1:])
        while steps:
            if dir == "R":
                x += 1
            elif dir == "U":
                y += 1
            elif dir == "L":
                x -= 1
            elif dir == "D":
                y -= 1
            else:
                print("Error")
                break
            if (y,x) != (0,0):
                a.add((y,x))
            steps -= 1
    return a

def manhattan(coords):
    man = []
    for c in coords:
        dist = abs(c[0]) + abs(c[1])
        if dist == 0:
            continue
        man.append(dist)
    return min(man)

def day(te):
    first = []
    second = []
    for i in te[0].split(","):
        first.append(i)
    for i in te[1].split(","):
        second.append(i)
    x = 0
    y = 0
    c1 = coordToSet(first)
    c2 = coordToSet(second)
    common = c1 & c2
    return manhattan(common)

def stepsToPosition(instructions,position):
    x, y, s = 0, 0, 0
    while 1:
        for i in instructions:
            dir = i[0]
            steps = int(i[1:])
            while steps:
                if dir == "R":
                    x += 1
                elif dir == "U":
                    y += 1
                elif dir == "L":
                    x -= 1
                elif dir == "D":
                    y -= 1
                else:
                    print("Error")
                    break
                steps -= 1
                s += 1
                if (y,x) == position:
                    return s
    return s

def day2(te):
    first = []
    second = []
    for i in te[0].split(","):
        first.append(i)
    for i in te[1].split(","):
        second.append(i)
    x = 0
    y = 0
    c1 = coordToSet(first)
    c2 = coordToSet(second)
    common = c1 & c2
    firstmin = []
    secondmin = []
    for c in common:
        if c == (0,0):
            continue
        firstmin.append(stepsToPosition(first,c))
        secondmin.append(stepsToPosition(second,c))

    bothmin = [0]*len(firstmin)
    for i in range(len(bothmin)):
        bothmin[i] = firstmin[i] + secondmin[i]
    return min(bothmin)

'''     #######     '''

time0 = time.time()

if samp == 1:
    filename = "/sample.txt"
else:
    filename = "/input.txt"

try:
    with open(str(date) + filename,"r") as f:
        t = f.readlines()
except FileNotFoundError:
    with open("." + filename,"r") as f:
        t = f.readlines()

t = [(x.strip().replace('  ',' ')) for x in t]
if part == 1:
    print("Part 1: ", day(t))
elif part == 2:
    print("Part 2: ", day2(t))
elif part == 3:
    #run both
    print("Part 1: ", day(t))
    print("Part 2: ", day2(t))

tdif = time.time() - time0
print("Elapsed time: {:.4f} s".format(tdif))
