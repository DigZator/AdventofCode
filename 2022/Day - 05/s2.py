import re
import numpy as np
import string
import os

inputfile = os.getcwd() + "\\2022\Day - 05\input.txt"
lines = []
print(inputfile)

with open(inputfile) as f:
    for line in f.readlines():
        lines.append(line)

# print(lines)


# board = [(re.split(r"",line)) for line in lines[:9]]

board = [list() for _ in range(9)]
print(len(board[0]))
for line in lines[:8]:
    char_count = 0
    for char in line:
        char_count += 1
        # print(char)
        if(char != " " and (char_count % 4 == 2)):
            count = char_count // 4
            # print(count)
            board[count].insert(0,char)

print(board)

commands = lines[10:]
for i in range(len(commands)):
    commands[i] = (re.split(r'move | from | to ', commands[i]))
    commands[i] = [int(ch,10) for ch in commands[i] if ch != '']

print(commands)

for command in commands:
    n, f, t = command[0], command[1] - 1, command[2] - 1
    mv = []
    for i in range(n):
        mv.append(board[f].pop())
    for k in range(len(mv)):
        board[t].append(mv.pop())
print(board)

for col in board:
    print(col.pop(), end = "")