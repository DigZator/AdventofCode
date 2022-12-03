import string


points = {}
for l in (list(string.ascii_lowercase)):
     points[l] = ord(l)-ord("a")+1


for l in (list(string.ascii_uppercase)):
     points[l] = ord(l)-ord("A")+27


lines = []
with open("./2022/Day - 03/input.txt") as f:
    for line in f.readlines():
        lines.append(line.strip())

match = []
for i in range(0, len(lines), 3):
    l1, l2, l3 = lines[i:i+3]
    # print(l1, l2, l3, '\n')
    for p in l1:
        if (p in l2) and (p in l3):
            match.append(p)
            break
# print(match)
print(sum(map(lambda x: points[x], match)))