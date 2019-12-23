#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
from collections import defaultdict
#from collections import deque
'''     #######     '''

date = 10
dev = 0 # extra prints
part = 1 # 1,2, or 3 for both
samp = 1 # 0 or 1

'''     #######     '''


def day(te):
    d = defaultdict()
    asteroids = set() #asteroid coords as (row, col)
    for row in range(len(te)):
        print(te[row])
        d[row] = []
        for col in range(len(te[row])):
            i = te[row][col]
            if i == "#":
                asteroids.add((row,col))
            d[row].append(i)
    #print(d)
    print(asteroids)
    astId = []
    astMon = []
    for a in asteroids:
        r = a[0]
        c = a[1]
        x = 1
        y = 1
        m = 1
        dir = "R" #R, U, L, D
        while 1:
            try:
                if d[r+y*m][c+x*m] == "#":
                    print(r, c, m, "#")
                else:
                    print(r, c, m, ".")
            except:
                if dir == "R":
                    dir = "U"
                break
            m += 1

    return 0

def day2(te):

    return 0

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
