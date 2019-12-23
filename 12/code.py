#!/usr/bin/python3

#from collections import Counter
#import re
#import os
#import numpy as np
import time
from collections import defaultdict
#from collections import deque
'''     #######     '''

date = 12
dev = 0 # extra prints
part = 3 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def printMoons(s, p, v):
    print("After", s, "steps:")
    for i in range(4):
        posstr = "pos=" + str(p[i])
        velstr = "vel=" + str(v[i])
        print(posstr, ",", velstr)
    print(" ")
    return 0

def calcEnerg(p, v):
    Etot = 0
    for i in range(4):
        Ekin = 0
        Epot = 0
        for j in range(3):
            Ekin += abs(v[i][j])
            Epot += abs(p[i][j])
        Etot += Ekin*Epot
        #print(Epot, Ekin, Etot)
    return Etot

def day(te):
    pos = defaultdict(list)
    vel = defaultdict(list)
    id = 0 # Io, Europa, Ganymede, and Callisto
    for i in te:
        i = (i.replace("<", "").replace(">", "").replace(",", "").split(" "))
        x = int(i[0][2:])
        y = int(i[1][2:])
        z = int(i[2][2:])
        pos[id] = [x,y,z]
        vel[id] = [0,0,0]
        id += 1
    if samp:
        maxsteps = 100
    else:
        maxsteps = 1000
    step = 0
    #printMoons(step, pos, vel)
    while step < maxsteps:
        #update velocity
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                for k in range(3):
                    if pos[i][k] > pos[j][k]:
                        vel[i][k] -= 1
                    elif pos[i][k] < pos[j][k]:
                        vel[i][k] += 1
        #update position
        for i in range(4):
            for k in range(3):
                pos[i][k] += vel[i][k]
        step += 1
        #printMoons(step, pos, vel)

    return calcEnerg(pos, vel)

def getdata(p, v):
    d = []
    for i in range(4):
        d.append(p[i])
        d.append(v[i])
    return str(d)

def getdataXYZ(p, v, axis):
    d = []
    for i in range(4):
        d.append(p[i][axis])
        d.append(v[i][axis])
    return str(d)

def day2(te):

    energies = set()
    pos = defaultdict(list)
    vel = defaultdict(list)
    id = 0 # Io, Europa, Ganymede, and Callisto
    for i in te:
        i = (i.replace("<", "").replace(">", "").replace(",", "").split(" "))
        x = int(i[0][2:])
        y = int(i[1][2:])
        z = int(i[2][2:])
        pos[id] = [x,y,z]
        vel[id] = [0,0,0]
        id += 1
    if 0:
        maxsteps = 3000#4686774927
    else:
        maxsteps = 4686774927
    step = 0
    m = 0
    hits = [0,0,0]
    #printMoons(step, pos, vel)
    visitedx = set()
    visitedy = set()
    visitedz = set()
    #visited.add(getposdata(pos))
    #visited.add(getdata(pos, vel))
    #visitedx.add(getdataXYZ(pos, vel, 0))
    #visitedy.add(getdataXYZ(pos, vel, 1))
    #visitedz.add(getdataXYZ(pos, vel, 2))
    loopx = False
    loopy = False
    loopz = False

    while step < maxsteps:
        #update velocity
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                if not loopx:
                    if pos[i][0] > pos[j][0]:
                        vel[i][0] -= 1
                    elif pos[i][0] < pos[j][0]:
                        vel[i][0] += 1
                if not loopy:
                    if pos[i][1] > pos[j][1]:
                        vel[i][1] -= 1
                    elif pos[i][1] < pos[j][1]:
                        vel[i][1] += 1
                if not loopz:
                    if pos[i][2] > pos[j][2]:
                        vel[i][2] -= 1
                    elif pos[i][2] < pos[j][2]:
                        vel[i][2] += 1
        #update position
        for i in range(4):
            for k in range(3):
                pos[i][k] += vel[i][k]


        if not loopx:
            datax = getdataXYZ(pos, vel, 0)
            if datax in visitedx:
                loopx = True
                hits[0] = step
                print("x:", step)
            else:
                visitedx.add(datax)
        if not loopy:
            datay = getdataXYZ(pos, vel, 1)
            if datay in visitedy:
                loopy = True
                hits[1] = step
                print("y:", step)
            else:
                visitedy.add(datay)
        if not loopz:
            dataz = getdataXYZ(pos, vel, 2)
            if dataz in visitedz:
                loopz = True
                hits[2] = step
                print("z:", step)
            else:
                visitedz.add(dataz)
        if (loopx and loopy and loopz):
            break
        step += 1
    #print(visitedx)
    #print(visited)
    #print(hits)

    return hits

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

t = [(x.strip()) for x in t]

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
