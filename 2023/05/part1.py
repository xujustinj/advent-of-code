from collections import defaultdict
import re

with open("2023/05/input.txt") as f:
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

seeds = parse_list(cleanup(lines[0], prefix_delimiter=":"))
locations = []

for seed in seeds:
    map_done = False
    for i, line in enumerate(lines[1:]):
        line = cleanup(line)
        if len(line) == 0 or line[-1] == ":":
            map_done = False
            continue
        if map_done:
            continue
        d, s, l = parse_list(line)
        if s <= seed < s+l:
            seed = seed - s + d
            map_done = True
    locations.append(seed)

print(min(locations))
