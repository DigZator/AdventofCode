import re
import numpy as np
import string
import os

file_year = "22"
file_date = "08"
inputfile = os.getcwd() + "\\20" + file_year + "\Day - " + file_date + "\input.txt"
lines = []
print(inputfile)

with open(inputfile) as f:
    lines = f.read().strip().split()

# print(lines)
grid = [list(map(int, list(line))) for line in lines]
print(grid)

grid = np.array(grid)
m , n = grid.shape

ans = 0

for i in range(1, n-1):
    for j in range(1, m-1):
        u, d, l, r = 1, 1, 1, 1
        h = grid[i][j]
        while (i-u >= 0 and grid[i-u][j] < h):
            u += 1
        while (i+d < n and grid[i+d][j] < h):
            d += 1
        while (j-l >= 0 and grid[i][j-l] < h):
            l += 1
        while (j+r < m and grid[i][j+r] < h):
            r += 1
        u = u-1 if i-u  < 0 else u
        d = d-1 if i+d > n-1 else d
        l = l-1 if j-l < 0 else l
        r = r-1 if j+r > m-1 else r
        print(i, j , u*d*l*r, u, d, l, r)
        ans = max(ans, u*d*l*r)


print(ans)
            