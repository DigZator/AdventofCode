import re
import numpy as np
import string
import os

file_year = "22"
file_date = "09"
inputfile = os.getcwd() + "\\20" + file_year + "\Day - " + file_date + "\input.txt"
print(inputfile)

with open(inputfile) as f:
    com = f.read().strip().split("\n")
# print(com)

coms = []
for c in com:
    coms.append([c[0], int(c[2:])])
# print(coms)

H = [0, 0]
T = [0, 0]
visit = set()

neigh = [[i, j] for i in range(-1,2) for j in range(-1,2) if not (i == j and i == 0)]

def inrange(H, T):
    difx = abs(H[0] - T[0])
    dify = abs(H[1] - T[1])

    if (difx < 2 and dify < 2):
        return (0, 0)
    elif (difx == 0 or dify == 0):
        return (0, 1 if H[1] > T[1] else -1) if difx == 0 else (1 if H[0] > T[0] else -1, 0)
    else:
        a = 1 if H[0] > T[0] else -1
        b = 1 if H[1] > T[1] else -1
        return (a,b)

for com in coms:
    direc, length = com
    for step in range(length):
        if direc == "U":
            H[1] += 1
        elif direc == "D":
            H[1] = H[1] - 1
        elif direc == "L":
            H[0] = H[0] - 1
        elif direc == "R":
            H[0] += 1
        
        a, b = inrange(H, T)
        T = (T[0] + a, T[1] + b)
        visit.add(T)

# print(visit)
print(len(visit))
