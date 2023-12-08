from collections import defaultdict
import re

number_re = re.compile("\d+")
symbol_re = re.compile(".*[^.\d].*")

acc: int = 0

with open("2023/03/input.txt") as f:
    lines = f.readlines()

adjacent = defaultdict(list)

for i, line in enumerate(lines):
    line = line.strip()
    for match in number_re.finditer(line):
        j = match.start()
        l = len(match.group())
        imin = max(0,i-1)
        imax = min(len(lines)-1,i+1)
        jmin = max(0,j-1)
        jmax = min(len(line)-1,j+l)
        for ii in range(imin,imax+1):
            for jj in range(jmin,jmax+1):
                if lines[ii][jj] == "*":
                    adjacent[(ii,jj)].append(int(match.group()))

for item in adjacent.values():
    if len(item) == 2:
        acc += item[0] * item[1]

print(acc)
