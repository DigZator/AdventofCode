import numpy
import os
import re

day = "01"
fileloc = os.getcwd() + f"\\2023\\Day - {day}\\input.txt"

with open(fileloc) as f:
    lines = [line.strip() for line in f.readlines()]

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0
for i in range(len(lines)):
    line = lines[i]
    fir = None
    las = None

    for i in range(len(line)):
        cur = None
        c = line[i]

        if c.isdigit():
            cur = int(c)
        
        for j, num in enumerate(nums):
            if line[i:i+len(num)] == num:
                cur = j + 1
                break
        if cur:
            if fir == None:
                fir = cur
            last = cur
    sum += fir*10 + last
        
# print(lines)
print("\n\n", sum)