#!/usr/bin/python3

import time

'''     #######     '''

date = 5
dev = 0 # extra prints
part = 1 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''


def day(te):
    a = []
    for i in te[0].split(","):
        a.append(int(i))
    idx = 0
    puzInput = 1
    puzOutputs = set()
    print(len(a))
    print(a)
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
            puzOut = a[a[idx+1]] if mode1 else a[a[idx+1]]
            if puzOut:
                puzOutputs.add(puzOut)
            print("Output: ", puzOut)
            idx += 2
        elif instr == 99:
            print("Program done.")
            break
        else:
            print("Error, unknown instruction: ", instr)
            break
    if dev:
        print(a)
    return puzOutputs

def day2(te):
    b = []
    for i in te[0].split(","):
        b.append(int(i))
    ans = 19690720
    for n in range(0, 100):
        for v in range(0, 99):
            val = func(b[:], n, v)
            #print(n, v, val)
            if val == ans:
                return (100*n+v)
    return 1

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
