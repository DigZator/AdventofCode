import numpy as np

if __name__ == "__main__":
    lines = []
    col = []

    with open("./2022/Day - 01/input.txt") as f:
        for line in f.readlines():
            lines.append(line.strip())
            # print(col)
    
    elfs = []
    s = 0
    for l in lines:
        if l == "":
            elfs.append(s)
            s = 0
        else:
            s = s + int(l,10)
    
    print(sum(sorted(elfs)[-3:]))