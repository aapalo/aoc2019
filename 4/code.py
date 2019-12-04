#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
#from collections import defaultdict
#from collections import deque
'''     #######     '''

date = 4
dev = 0 # extra prints
part = 3 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def increases(p):
    j = str(p)
    for i in range(len(j)-1):
        if j[i] <= j[i+1]:
            continue
        else:
            return 0
    return 1

def hasDouble(p):
    j = str(p)
    for i in range(len(j)-1):
        if j[i] == j[i+1]:
            return 1
    return 0

def day(te):
    if samp:
        pw = [111111, 223450, 123789]
    else:
        pw = list(range(382345,843167+1))
    poss = 0
    for i in pw:
        if increases(i):
            if hasDouble(i):
                poss += 1
    return poss

def hasOneDouble(p):
    j = list(str(p))
    hd = False
    # how many times a number appears in the list
    for i in range(0,10):
        if (sum(s == str(i) for s in j)) == 2:
            hd = True
    return hd

def day2(te):
    if samp:
        pw = [112233, 123444, 111122, 566688, 111223, 112223]
    else:
        pw = list(range(382345,843167+1))
    poss = 0
    for i in pw:
        if(increases(i)):
            if hasOneDouble(i):
                poss += 1
    return poss

'''     #######     '''

time0 = time.time()
t = 0
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
