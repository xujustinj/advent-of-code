from math import lcm

with open("2023/08/input.txt") as f:
    lines = f.readlines()

moves = lines[0].strip()

map = {}
for line in lines[2:]:
    k, v = line.strip().split(" = ")
    l, r = v.strip("()").split(", ")
    map[k] = (l, r)

def steps(pos: str) -> int:
    i = 0
    while pos[-1] != "Z":
        if moves[i % len(moves)] == "L":
            pos, _ = map[pos]
        else:
            _, pos = map[pos]
        i += 1
    return i

print(lcm(*(steps(pos) for pos in map.keys() if pos[-1] == "A")))
