import numpy
import os
import re

day = "03"
fileloc = os.getcwd() + f"\\2023\\Day - {day}\\input.txt"

with open(fileloc) as f:
    lines = [line.strip() for line in f.readlines()]

# print(lines)
m, n = (len(lines), len(lines[0]))

def is_symbol(i, j):
    if not (0 <= i < m and 0 <= j < n):
        return False
    return lines[i][j] != "." and not lines[i][j].isdigit()


ans = 0
for i in range(m):
    j = 0
    while j < n:
        if lines[i][j].isdigit():
            num = (lines[i][j])
            cur = j+1
            toadd = False
            while cur < n and lines[i][cur].isdigit():
                num += lines[i][cur]
                cur += 1
            # print(num, j, cur)
            if is_symbol(i, j-1) or is_symbol(i, cur):
                toadd = True
            for k in range(j-1, cur+1):
                if is_symbol(i-1, k) or is_symbol(i+1, k):
                    toadd = True
            j = cur
            if toadd:
                ans += int(num)
        j += 1
print(ans)