import re
import numpy as np
import string
import os

file_year = "22"
file_date = "10"
inputfile = os.getcwd() + "\\20" + file_year + "\Day - " + file_date + "\input.txt"
lines = []
print(inputfile)

with open(inputfile) as f:
    for line in f.readlines():
        lines.append(line.strip())

print(lines)
s = 0
x = 1
i = 0
check = [20, 60, 100, 140, 180, 220]
for com in (lines):
    if com[0] == "n":
        i += 1
        if i in check:
            s += x*i
    else:
        v = int(com[4:])
        x += v
        i += 1
        if i in check:
            s += i*(x-v)
        i += 1
        if i in check:
            s += i*(x-v)
print(i)
print(s)