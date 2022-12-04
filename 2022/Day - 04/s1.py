import re

pairs = []

with open("./2022/Day - 04/input.txt") as f:
    for line in f.readlines():
        line = (re.split(r"-|,", line))
        pair = []
        for a in line:
            pair.append(int(a, 10))
        pairs.append(pair)
count = 0
for pair in pairs:
    s1, e1, s2, e2 = pair
    if (s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1):
        count += 1
print(count)    