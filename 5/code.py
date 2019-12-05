#!/usr/bin/python3

import time

'''     #######     '''

date = 5
dev = 0 # extra prints
part = 1 # 1,2, or 3 for both
samp = 1 # 0 or 1

'''     #######     '''


def day(te):
    a = []
    for i in te[0].split(","):
        a.append(int(i))
    idx = 0
    if not samp:
        a[1] = 12
        a[2] = 2
    while idx < len(a):
        print(a[idx])
        instr = a[idx]
        if instr == 1:
            # add
            a[a[idx+3]] = a[a[idx+1]] + a[a[idx+2]]
            idx += 4
        elif instr == 2:
            a[a[idx+3]] = a[a[idx+1]] * a[a[idx+2]]
            idx += 4
        elif instr == 3:
            a[a[idx+3]] = a[a[idx+1]] * a[a[idx+2]]
            idx += 4
        elif instr == 4:
            a[a[idx+3]] = a[a[idx+1]] * a[a[idx+2]]
            idx += 4
        elif instr == 99:
            break
        idx += 1
    return a[0]

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
