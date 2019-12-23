#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
from collections import defaultdict
#from collections import deque
'''     #######     '''

date = 6
dev = 0 # extra prints
part = 3 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def calcOrbits(dict, i):
    s = len(dict[i])
    orbs = []
    for j in dict[i]:
        s += calcOrbits(dict, j)
        orbs.append(j)
    if samp:
        print(orbs)
    return s

def day(te):
    objects = set()
    objects2 = set()
    rd = defaultdict(list)
    for p in te:
        p = p.split(",")
        m = p[0]
        c = p[1]
        objects.add(m)
        objects2.add(c)
        rd[c].append(m)

    orbsum = 0
    for j in objects.union(objects2):
        co = calcOrbits(rd, j)
        orbsum += co
    return orbsum

def calcRoute(dict, i, orbs):
    for j in dict[i]:
        orbs.add(calcRoute(dict, j, orbs))
    return i

def day2(te):
    objects = set()
    objects2 = set()
    rd = defaultdict(list)
    for p in te:
        p = p.split(",")
        m = p[0]
        c = p[1]
        objects.add(m)
        objects2.add(c)
        rd[c].append(m)

    orbSAN = set()
    calcRoute(rd, "SAN", orbSAN)
    orbYOU = set()
    calcRoute(rd, "YOU", orbYOU)

    # exclude common items
    orbBoth = orbSAN^(orbYOU)
    return len(orbBoth)

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

t = [(x.strip().replace(')',',')) for x in t]

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
