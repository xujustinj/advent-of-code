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

acc: int = 0

time = int("".join(c for c in cleanup(lines[0]) if c.isnumeric()))
dist = int("".join(c for c in cleanup(lines[1]) if c.isnumeric()))

def day6part2(time, dist):
    disc = time * time - 4 * dist
    if disc <= 0:
        return 0
    s = math.sqrt(disc)
    l = int(math.ceil((time - s) / 2))
    r = int(math.floor((time + s) / 2))
    return r - l + 1

print(day6part2(time, dist))
