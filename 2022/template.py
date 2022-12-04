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

print(lines)