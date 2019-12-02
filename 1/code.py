#!/usr/bin/python3

import time

'''     #######     '''

date = 1
dev = 0 # extra prints
part = 3 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''
def day(te):
    fuelsum = 0
    for i in te:
        try:
            i = int(i)
            fuel = int(i/3) -2
            fuelsum += fuel
            #print(i,fuel)
        except:
            pass
    return fuelsum

def day2(te):
    fuelsum = 0
    for idx in range(len(te)):
        try:
            i = int(te[idx])
        except:
            pass
        while (i > 0):
            fuel = int(i/3) -2
            i = fuel
            if samp:
                print(fuel)
            if i > 0:
                fuelsum += fuel
            else:
                i = 0
                fuel = 0
                break
        if samp:
            print(idx, te[idx],fuelsum)

    return fuelsum

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

t = [(x.strip().replace('<->','').replace(',','').replace('  ',' ')) for x in t]
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
