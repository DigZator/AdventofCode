
lines = []
with open("./2022/Day - 02/input.txt") as f:
    for line in f.readlines():
        lines.append(line.strip())

# print(lines)
plays = []
for play in lines:
    plays.append(play[0] + play[2])

op = ["A", "B", "C"]
pp = ["X", "Y", "Z"]

combs = {}

for no, o in enumerate(op):
    for np, p in enumerate(pp):
        points = 0
        if no == np:
            points = (no+1) + 3
        elif ((no+1)%3 == np):
            points = (np + 1) + 6
        else:
            points = (np+1)
        combs[o + p] = points
score = 0
for play in plays:
    score += combs[play]
print(score)
