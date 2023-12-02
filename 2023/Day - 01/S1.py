import numpy
import os
import re

day = "01"
fileloc = os.getcwd() + f"\\2023\\Day - {day}\\input.txt"

with open(fileloc) as f:
    lines = [line.strip() for line in f.readlines()]

sum = 0
for i in range(len(lines)):
    lines[i] = re.sub(r"[a-zA-Z]", "", lines[i])
    sum += int(lines[i][0] + lines[i][-1])

print(sum)
