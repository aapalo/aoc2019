#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
#from collections import defaultdict
#from collections import deque
'''     #######     '''

date = 22
dev = 0 # extra prints
part = 2 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def cut(dek, idx):
    first = dek[:idx]
    del dek[:idx]
    dek.extend(first)
    return dek

def deal(dek, inc):
    dek2 = [0]*len(dek)
    idx = 0
    deklen = len(dek)
    dek = stack(dek)
    while 1:
        try:
            dek2[idx] = dek.pop()
        except IndexError:
            #empty list
            break
        #print(dek2, idx)
        idx += inc
        if idx > deklen:
            idx = idx % deklen
    return dek2

def stack(dek):
    return dek[::-1]

def day(te):
    decksize = 10
    if not samp:
        decksize = 10007
    deck = list(range(decksize))
    #print(deck)
    for i in te:
        i = i.split()
        #print(i)
        if "cut" == i[0]:
            deck = cut(deck, int(i[1]))
        elif "increment" == i[2]:
            deck = deal(deck, int(i[3]))
        elif "stack" == i[3]:
            deck = stack(deck)
    print(deck)
    if samp:
        return deck.index(0)
    else:
        return deck.index(2019)

def day2(te):
    decksize = 10
    if not samp:
        decksize = 119315717514047
    deck = list(range(decksize))
    #print(deck)
    for j in range(101741582076661):
        for i in te:
            i = i.split()
            #print(i)
            if "cut" == i[0]:
                deck = cut(deck, int(i[1]))
            elif "increment" == i[2]:
                deck = deal(deck, int(i[3]))
            elif "stack" == i[3]:
                deck = stack(deck)
    #print(deck)
    if samp:
        return deck[0]
    else:
        return deck[2020]

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
