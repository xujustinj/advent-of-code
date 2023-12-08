from collections import defaultdict
import math
import re

with open("2023/07/input.txt") as f:
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

def value(hand: list[int]):
    counts = defaultdict(int)
    for i in hand:
        counts[i] += 1
    common = sorted(((v, k) for k, v in counts.items()), reverse=True)
    t = common[0][0]
    if t > 3 or (t == 3 and common[1][0] == 2):
        t += 1
    if t > 2 or (t == 2 and common[1][0] == 2):
        t += 1
    return (t, *hand)

card_value = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

bets = []
for line in lines:
    hand, bet = parse_list(line, parse=str)
    val = value([card_value[c] for c in hand])
    print(hand, val)
    bets.append([val, int(bet)])

bets.sort()

for i, (val, bet) in enumerate(bets):
    print(val, bet)
    acc += (i+1) * bet

print(acc)
