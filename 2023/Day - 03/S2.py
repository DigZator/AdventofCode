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
    return lines[i][j] == "*"


def add_todic(i, j, num):
    if (i, j) in ans:
        ans[(i, j)].append(num)
    else:
        ans[(i, j)] = [num]

ans = {}
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
            if is_symbol(i, j-1):
                add_todic(i, j-1, num)
            if is_symbol(i, cur):
                add_todic(i, cur, num)
                
            for k in range(j-1, cur+1):
                if is_symbol(i-1, k):
                    add_todic(i-1, k, num)
                if is_symbol(i+1, k):
                    add_todic(i+1, k, num)
                
            j = cur
        j += 1
print(ans)
ret = 0
for key in ans.keys():
    if len(ans[key]) != 2:
        continue
    a = 1
    for num in ans[key]:
        a = a*int(num)
    # print(a)
    ret += a

print(ret)