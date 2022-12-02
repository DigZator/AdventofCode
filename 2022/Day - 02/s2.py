
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
        points = []
        if no == np:
            points = [(no+1) + 3, "Y"]
        elif ((no+1)%3 == np):
            points = [(np + 1) + 6, "X"]
        else:
            points = [(np+1), "Z"]
        combs[o + p] = points
score = 0
for play in plays:
    opp = play[0]
    s = play[1]
    no = op.index(opp)
    if s == "X":
        plp = pp[(2+no)%3]
    elif s == "Y":
        plp = pp[no]
    else:
        plp = pp[(no+1)%3]
    score += combs[opp+plp][0]

print(score)
