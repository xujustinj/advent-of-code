from collections import defaultdict
import re

with open("2023/04/input.txt") as f:
    lines = f.readlines()

acc: int = 0

for i, line in enumerate(lines):
    line = line.strip()
    _, line = line.split(":")
    target, actual = line.split("|")
    target = set(int(n) for n in target.split() if n.isnumeric())
    actual = set(int(n) for n in actual.split() if n.isnumeric())
    winning = len(target & actual)
    if winning > 0:
        acc += 2 ** (winning - 1)

print(acc)
