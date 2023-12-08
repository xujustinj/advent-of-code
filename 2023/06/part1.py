from collections import defaultdict
import math
import re

with open("2023/06/input.txt") as f:
    lines = f.readlines()

def cleanup(
        line: str,
        prefix_delimiter: str | None = None,
) -> str:
    line = line.strip()
    if prefix_delimiter is not None:
        _, line = re.split(prefix_delimiter, line, maxsplit=1)
        line = line.strip()
    return line

def parse_list(
        line: str,
        delimiter: str = " ",
        parse = int,
) -> list:
    words = line.strip().split(delimiter)
    return [parse(word) for word in words if len(word) > 0]

acc: int = 1

times = parse_list(cleanup(lines[0], prefix_delimiter=":"))
distances = parse_list(cleanup(lines[1], prefix_delimiter=":"))

for t, d in zip(times, distances):
    count = 0
    for ti in range(t):
        if ti * (t - ti) > d:
            count += 1
    acc *= count

print(acc)
