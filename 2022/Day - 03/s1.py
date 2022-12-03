match = []
import string
with open("./2022/Day - 03/input.txt") as f:
    for line in f.readlines():
        pre, suf = line[:len(line)//2], line[len(line)//2:]
        for p in pre:
            if p in suf:
                match.append(p)
                break
print(match)
points = {}
for l in (list(string.ascii_lowercase)):
     points[l] = ord(l)-ord("a")+1


for l in (list(string.ascii_uppercase)):
     points[l] = ord(l)-ord("A")+27

print(sum(map(lambda x: points[x], match)))