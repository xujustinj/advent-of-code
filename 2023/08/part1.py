with open("2023/08/input.txt") as f:
    lines = f.readlines()

moves = lines[0].strip()

map = {}

pos = "AAA"
for line in lines[2:]:
    k, v = line.strip().split(" = ")
    l, r = v.strip("()").split(", ")
    map[k] = (l, r)

i = 0
while pos != "ZZZ":
    if moves[i % len(moves)] == "L":
        pos, _ = map[pos]
    else:
        _, pos = map[pos]
    i += 1
    print(pos)

print(i)
