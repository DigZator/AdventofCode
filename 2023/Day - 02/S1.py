import numpy
import os

day = "02"
fileloc = os.getcwd() + f"\\2023\\Day - {day}\\input.txt"

with open(fileloc) as f:
    lines = [line.strip() for line in f.readlines()]

aldic = {}

colleg = {"red" : 0,
          "blue" : 2,
          "green" : 1}

for i in range(len(lines)):
    parts = lines[i].split(": ")
    print(parts)
    gamenum = int(parts[0].split(" ")[-1])
    rounds = parts[1].split("; ")
    aldic[gamenum] = []
    for round in rounds:
        roundret = [0, 0, 0]
        roundparts = round.split(", ")
        for j in range(len(roundparts)):
            roundret[colleg[roundparts[j].split(" ")[1]]] += int(roundparts[j].split(" ")[0])
        aldic[gamenum].append(roundret)
    aldic[gamenum] = numpy.array(aldic[gamenum])

for key in aldic.keys():
    print(f"Game {key}:")
    print(aldic[key])
    print()

lims = [12, 13, 14]

imp = []

for key in aldic.keys():
    for i in range(3):
        if aldic[key][:,i].max() > lims[i]:
            imp.append(key)
            break

print(imp)
print(sum(imp))
poss = [i for i in range(1, 101) if i not in imp]
print(poss)
print(sum(poss))