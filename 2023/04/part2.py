from collections import defaultdict
import re

with open("2023/04/input.txt") as f:
    lines = f.readlines()

acc: int = 0
counts = [1 for _ in lines]

for i, line in enumerate(lines):
    line = line.strip()
    _, line = line.split(":")
    target, actual = line.split("|")
    target = set(int(n) for n in target.split() if n.isnumeric())
    actual = set(int(n) for n in actual.split() if n.isnumeric())
    winning = len(target & actual)
    for j in range(winning):
        counts[i+1+j] += counts[i]

print(sum(counts))
