total = 0
with open("2023/01/input.txt") as f:
    for line in f.readlines():
        digits = [c for c in line if c.isnumeric()]
        total += int(digits[0] + digits[-1])
print(total)
