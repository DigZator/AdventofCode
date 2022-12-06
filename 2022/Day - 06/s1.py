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
# line1 = "_" + line
# line2 = "_" + line1
# line3 = "_" + line2

# last_rep = 0
# for i in range(3,len(line)):
#     lis = [line[i], line1[i], line2[i], line3[i]]
#     if len(set(lis)) == 4:
#         break
# i = i-2
# print(i, lis)
# print(line[i-1:i+3])

for i in range(len(line)-3):
    if len(set(line[i:i+4])) == 4:
        print(i + 4)
        break
    i += 1