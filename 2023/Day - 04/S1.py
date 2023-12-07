import numpy
import os

day = "04"
fileloc = os.getcwd() + f"\\2023\\Day - {day}\\input.txt"

with open(fileloc) as f:
    lines = [line.strip() for line in f.readlines()]

dat = {}
for i in range(len(lines)):
    line = lines[i]
    parts = line.split(": ")
    parts[0] = parts[0].split(" ")
    parts[1] = parts[1].split(" | ")
    parts[1][0] = [int(x) for x in parts[1][0].split(" ") if x != ""]
    parts[1][1] = [int(x) for x in parts[1][1].split(" ") if x != ""]
    dat[int(parts[0][-1])] = parts[1]

points = 0
print(dat)

for key in dat.keys():
    # print(key)
    # print(dat[key])
    mat = 0
    for i in range(len(dat[key][0])):
        if dat[key][0][i] in dat[key][1]:
            mat += 1
            print(dat[key][0][i], mat)
    if mat == 0:
        ret = 0
    else:
        ret = 2**(mat - 1)
    points += ret
    print(key, ret)

print(points)