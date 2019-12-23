#!/usr/bin/python3

import time
from collections import defaultdict
'''     #######     '''

date = 9
dev = 1 # extra prints
part = 1 # 1,2, or 3 for both
samp = 1 # 0 or 1

'''     #######     '''
def printdict(d):
    s = ""
    for i in d.keys():
        s += str(d[i]) + ","
    print(s)
    return 0

def day(te, puzInput):
    a = defaultdict(int)
    j = 0
    for i in te[0].split(","):
        a[j] = int(i)
        j += 1
    idx = 0
    relbase = 0
    puzOutputs = set()
    while idx < j:
        if 1:
            printdict(a)
        if 1:
            print(relbase, idx, a[idx])

        i = str(a[idx])
        while len(i) < 5:
            i = '0' + i
        instr = int(i[3:])
        mode1 = int(i[2])
        mode2 = int(i[1])
        mode3 = int(i[0])
        try:
            #p1 = a[idx+1] if mode1 else a[a[idx+1]]
            if mode1 == 1:
                p1 = a[idx+1]
            elif mode1 == 0:
                p1 = a[a[idx+1]]
            else:
                p1 = a[a[idx+1+relbase]]
            if mode2 == 1:
                p2 = a[idx+2]
            elif mode2 == 0:
                p2 = a[a[idx+2]]
            else:
                p2 = a[a[idx+2+relbase]]
            if mode3 == 1:
                p3 = a[idx+3]
            elif mode3 == 0:
                p3 = a[a[idx+3]]
            else:
                p3 = a[a[idx+3+relbase]]
            p3 = a[idx+3]
        except IndexError:
            pass
        if 1:
            print(i, mode1, mode2, mode3, instr)
            print("p1-3:", p1, p2, p3)
        if instr == 1:
            # add
            #a[a[idx+3]] = p1 + p2
            a[p3] = p1 + p2
            idx += 4
        elif instr == 2:
            #a[a[idx+3]] = p1 * p2
            a[p3] = p1 * p2
            idx += 4
        elif instr == 3:
            #a[a[idx+1]] = puzInput
            a[p1] = puzInput
            idx += 2
        elif instr == 4:
            puzOut = p1
            puzOutputs.add(puzOut)
            idx += 2
        elif instr == 5:
            idx = p2 if (p1 != 0) else (idx+3)
        elif instr == 6:
            idx = p2 if (p1 == 0) else (idx+3)
        elif instr == 7:
            #a[a[idx+3]] = 1 if (p1 < p2) else 0
            a[p3] = 1 if (p1 < p2) else 0
            idx += 4
        elif instr == 8:
            #a[a[idx+3]] = 1 if (p1 == p2) else 0
            a[p3] = 1 if (p1 == p2) else 0
            idx += 4
        elif instr == 9:
            relbase += p1
            idx += 2
        if instr == 99:
            #print("Program done.")
            break
    if 0:
        print(a)
    return puzOutputs

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

t = [(x.strip().replace('<->','').replace('  ',' ')) for x in t]
pin = 1

if part == 1:
    print("Part 1: ", day(t, 1))
elif part == 2:
    print("Part 2: ", day(t, 5))
elif part == 3:
    #run both
    part = 1
    print("Part 1: ", day(t, 1))
    part = 2
    print("Part 2: ", day(t, 5))

if samp:
    pin = [0,3,6,9]
    for p in pin:
        print(p, day(t, p))

tdif = time.time() - time0
print("Elapsed time: {:.4f} s".format(tdif))
