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
seeds = list((s, s+l) for s, l in zip(seeds[0::2], seeds[1::2]))
print(seeds)
locations = []

split_ids = [i for i in range(len(lines)) if lines[i] == "\n"] + [len(lines)]

for start, end in zip(split_ids[:-1], split_ids[1:]):
    new_seeds = []
    for line in lines[start+2:end]:
        ds, ss, l = parse_list(line)
        se = ss + l
        o = ds - ss
        next_seeds = []
        for s, e in seeds:
            if s in range(ss, se):
                if e-1 in range(s, e):
                    new_seeds.append((s+o,e+o))
                else:
                    new_seeds.append((s+o,se+o))
                    next_seeds.append((se, e))
            elif ss in range(s, e):
                next_seeds.append((s, ss))
                if e-1 in range(ss, se):
                    new_seeds.append((ss+o, e+o))
                else:
                    new_seeds.append((ss+o, se+o))
                    next_seeds.append((se, e))
            else:
                next_seeds.append((s, e))
        seeds = list(next_seeds)

    seeds += new_seeds

print(min(s for s, _ in seeds))
