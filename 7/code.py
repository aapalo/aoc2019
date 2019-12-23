#!/usr/bin/python3

import time
import itertools as iter
'''     #######     '''

date = 7
dev = 0 # extra prints
part = 1 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def intcode(te, puzInput):
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
        try:
            p1 = a[idx+1] if mode1 else a[a[idx+1]]
            p2 = a[idx+2] if mode2 else a[a[idx+2]]
        except IndexError:
            pass
        if dev:
            print(a)
            print(a[idx:(idx+4)], instr)
        if 0:
            print(i, mode1, mode2, mode3, instr)
        if instr == 1:
            # add
            a[a[idx+3]] = p1 + p2
            idx += 4
        elif instr == 2:
            a[a[idx+3]] = p1 * p2
            idx += 4
        elif instr == 3:
            a[a[idx+1]] = puzInput.pop()
            #print("Input", a[a[idx+1]])
            idx += 2
        elif instr == 4:
            puzOut = a[idx+1] if mode1 else a[a[idx+1]]
            puzOutputs.add(puzOut)
            #print("Output: ", puzOut)
            idx += 2
        elif instr == 5:
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
        elif instr == 99:
            #print("Program done.")
            break
    if dev:
        print(a)
    return puzOutputs.pop()


def day(te):
    sequence = [4,3,2,1,0]
    per = (iter.permutations(sequence))
    #per = [[3,1,2,4,0],[3,1,2,0,4]]
    signals = set()
    setting = 0
    for p in per:
    #    (p[1])
        setting = intcode(te,[setting,p[0]])
        setting = intcode(te,[setting,p[1]])
        setting = intcode(te,[setting,p[2]])
        setting = intcode(te,[setting,p[3]])
        setting = intcode(te,[setting,p[4]])
        signals.add(setting)
        #print(p, setting)
        setting = 0
    return max(signals)

def day2(te):
    sequence = [5,6,7,8,9]
    #per = (iter.permutations(sequence))
    per = [[5,6,7,8,9],[5,9,7,8,6]]
    signals = set()
    setting = 0
    for p in per:
    #    (p[1])
        setting = intcode(te,[setting,p[0]])
        setting = intcode(te,[setting,p[1]])
        setting = intcode(te,[setting,p[2]])
        setting = intcode(te,[setting,p[3]])
        setting = intcode(te,[setting,p[4]])
        signals.add(setting)
        print(p, setting)
        setting = 0
    return max(signals)

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
    print("Part 1: ", day(t))
elif part == 2:
    print("Part 2: ", day(t))
elif part == 3:
    #run both
    part = 1
    print("Part 1: ", day(t))
    part = 2
    print("Part 2: ", day(t))

tdif = time.time() - time0
print("Elapsed time: {:.4f} s".format(tdif))
