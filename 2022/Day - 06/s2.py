import re
import numpy as np
import string
import os

inputfile = os.getcwd() + "\\2022\Day - 06\input.txt"
lines = []
print(inputfile)

with open(inputfile) as f:
    for line in f.readlines():
        lines.append(line)

line = lines[0]
print(line)

for i in range(len(line)-13):
    if len(set(line[i:i+14])) == 14:
        print(i + 14)
        break
    i += 1