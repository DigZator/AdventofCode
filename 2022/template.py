import re
import numpy as np
import string
import os

file_year = "22"
file_date = "06"
inputfile = os.getcwd() + "\\20" + file_year + "\Day - " + file_date + "\input.txt"
lines = []
print(inputfile)

with open(inputfile) as f:
    for line in f.readlines():
        lines.append(line)

print(lines)