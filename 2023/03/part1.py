import re

number_re = re.compile("\d+")
symbol_re = re.compile(".*[^.\d].*")

acc: int = 0

with open("2023/03/input.txt") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    line = line.strip()
    for match in number_re.finditer(line):
        j = match.start()
        l = len(match.group())
        imin = max(0,i-1)
        imax = min(len(lines)-1,i+1)
        jmin = max(0,j-1)
        jmax = min(len(line)-1,j+l)
        surroundings = "".join(_line[jmin:jmax+1] for _line in lines[imin:imax+1])
        ok = symbol_re.match(surroundings) is not None
        print(i, j, surroundings, ok)
        if ok:
            acc += int(match.group())

print(acc)
