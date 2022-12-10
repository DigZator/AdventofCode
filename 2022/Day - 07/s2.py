import re
import numpy as np
import string
import os
from collections import defaultdict
from functools import lru_cache

file_year = "22"
file_date = "07"
inputfile = os.getcwd() + "\\20" + file_year + "\Day - " + file_date + "\input.txt"
lines = []
print(inputfile)

with open(inputfile) as f:
    lines = ('\n' + f.read().strip()).split("\n$ ")[1:]

path = []
dir_size = defaultdict(int)
child = defaultdict(list)
visited = set()

def parse(block):
    lines = block.split("\n")
    command = lines[0]
    op = lines[1:]
    oper = command.split(" ")[0]
    if oper == "cd":
        if command.split(" ")[1] == "..":
            path.pop()
        else:
            path.append(command.split(" ")[1])
        return
    
    abspath = "/".join(path)
    assert oper == "ls"

    sizes = []

    for line in op:
        # print(line)
        if line.startswith("dir"):
            st, name = line.split(" ")
            child[abspath].append(f"{abspath}/{name}")
        else:
            st, name = line.split(" ")
            sizes.append(int(st))
    dir_size[abspath] = sum(sizes)

    # print(command, op)
blocks = lines
for block in blocks:
    parse(block)

# print(dir_size)
@lru_cache(None)
def dfs(abspath):
    size = dir_size[abspath]
    for ch in child[abspath]:
        size += dfs(ch)
    return size

unused = 70000000 - dfs('/')
required = 30000000 - unused
print(unused)
ans = 1 << 60
for abspath in list(dir_size):
    s = dfs(abspath)
    if s >= required:
        ans = min(ans, s)
print(ans)