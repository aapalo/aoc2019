#!/usr/bin/python3

import time

'''     #######     '''

date = 5
dev = 0 # extra prints
part = 3 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def day(te, puzInput):
    a = []
    for i in te[0].split(","):
        a.append(int(i))
    idx = 0
    puzOutputs = set()
    while idx < len(a):
        #print(a[idx])
        i = str(a[idx])
        while len(i) < 5:
            i = '0' + i
        instr = int(i[3:])
        mode1 = int(i[2])
        mode2 = int(i[1])
        mode3 = int(i[0])
        if dev:
            print(a)
            print(a[idx:(idx+4)], instr)
        if 0:
            print(i, mode1, mode2, mode3, instr)
        if instr == 1:
            # add
            p1 = a[idx+1] if mode1 else a[a[idx+1]]
            p2 = a[idx+2] if mode2 else a[a[idx+2]]
            a[a[idx+3]] = p1 + p2
            idx += 4
        elif instr == 2:
            p1 = a[idx+1] if mode1 else a[a[idx+1]]
            p2 = a[idx+2] if mode2 else a[a[idx+2]]
            a[a[idx+3]] = p1 * p2
            idx += 4
        elif instr == 3:
            a[a[idx+1]] = puzInput
            idx += 2
        elif instr == 4:
            puzOut = a[idx+1] if mode1 else a[a[idx+1]]
            puzOutputs.add(puzOut)
            #print("Output: ", puzOut)
            idx += 2
        elif part > 1:
            try:
                p1 = a[idx+1] if mode1 else a[a[idx+1]]
                p2 = a[idx+2] if mode2 else a[a[idx+2]]
            except IndexError:
                pass
            if instr == 5:
                idx = p2 if p1 != 0 else (idx+3)
            elif instr == 6:
                idx = p2 if p1 == 0 else (idx+3)
            elif instr == 7:
                #p3 = a[idx+3] if mode3 else a[a[idx+3]]
                a[a[idx+3]] = 1 if (p1 < p2) else 0
                idx += 4
            elif instr == 8:
                #p3 = a[idx+3] if mode3 else a[a[idx+3]]
                a[a[idx+3]] = 1 if (p1 == p2) else 0
                idx += 4
        if instr == 99:
            #print("Program done.")
            break
    if dev:
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
    pin = [0,2,4,6,8,10]
    for p in pin:
        print(p, "Sample: ", day(t, p))

tdif = time.time() - time0
print("Elapsed time: {:.4f} s".format(tdif))
