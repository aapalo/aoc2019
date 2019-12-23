#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
from collections import defaultdict
#from collections import deque
'''     #######     '''

date = 8
dev = 1 # extra prints
part = 2 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def printpic(im, ph, pw):
    for r in range(ph):
        row = ""
        for c in range(pw):
            if im[r][c] == 0:
                row += (" ")
            elif im[r][c] == 1:
                row += ("X")
            elif im[r][c] == 2:
                row += (" ")
        print(row)
    return 0

def day(te, parttwo):
    if samp:
        if not parttwo:
            pw = 3 #pixel width
            ph = 2 #pixel height
        else:
            pw = 2 #pixel width
            ph = 2 #pixel height
    else:
        pw = 25 #pixel width
        ph = 6 #pixel height
    i = 0
    row = 0
    col = 0
    layers = int(len(te)/(pw*ph))
    pix = defaultdict(list)
    for p in range(layers):
        pix[p] = defaultdict(list)
        for r in range(ph):
            pix[p][r] = defaultdict(int)
            for c in range(pw):
                pix[p][r][c] = 0

    l = 0
    for p in te:
        #print(row, col)
        pix[l][row][col] = int(p)#.append(int(p))
        col += 1
        if col+1 > pw:
            row += 1
            col = 0
            if row+1 > ph:
                row = 0
                l += 1
    if not parttwo:
        minzeros = pw*ph
        minzlayer = 0
        values = defaultdict(list) #store amount of [0,1,2] per layer
        for p in pix.keys():
            values[p] = [0,0,0]
            zeros = 0
            for r in pix[p].keys():
                for c in pix[p][r].keys():
                    digit = (pix[p][r][c])
                    if digit == 0:
                        values[p][0] += 1
                        zeros += 1
                    elif digit == 1:
                        values[p][1] += 1
                    elif digit == 2:
                        values[p][2] += 1
            if zeros < minzeros:
                minzlayer = p
                minzeros = zeros
        #print(values)
        ans = values[minzlayer][1]*values[minzlayer][2]
        return ans
    # 0 black
    # 1 white
    # 2 transparent
    #for l in pix.keys():
    #    print(pix[l])
    image = defaultdict()
    for r in range(ph):
        image[r] = defaultdict(int)
        for c in range(pw):
            image[r][c] = 2
    #for l in image.keys():
    #print(image)
    #printpic(image, ph, pw)
    for r in range(ph):
        for c in range(pw):
            for p in range(layers):
                if image[r][c] != 2:
                    continue
                else:
                    image[r][c] = pix[p][r][c]
            #printpic(image, ph, pw)
            #print("-----")
    printpic(image, ph, pw)
    ans = 0
    return ans

'''
X     X  X   XX   XXX   X  X
X     X  X  X  X  X  X  X  X
X     XXXX  X     X  X  XXXX 
X     X  X  X     XXX   X  X
X     X  X  X  X  X     X  X
XXXX  X  X   XX   X     X  X
'''

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
t = t[0]
if part == 1:
    print("Part 1: ", day(t, 0))
elif part == 2:
    print("Part 2: ", day(t, 1))
elif part == 3:
    #run both
    print("Part 1: ", day(t, 0))
    print("Part 2: ", day(t, 1))

tdif = time.time() - time0
print("Elapsed time: {:.4f} s".format(tdif))
