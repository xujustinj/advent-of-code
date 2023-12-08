import re

digit_re = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")

def parse(digit: str) -> int:
    if digit == "one":
        return 1
    if digit == "two":
        return 2
    if digit == "three":
        return 3
    if digit == "four":
        return 4
    if digit == "five":
        return 5
    if digit == "six":
        return 6
    if digit == "seven":
        return 7
    if digit == "eight":
        return 8
    if digit == "nine":
        return 9
    return int(digit)

total: int = 0
with open("2023/01/input.txt") as f:
    for line in f.readlines():
        digits: list[str] = digit_re.findall(line)
        total += 10 * parse(digits[0]) + parse(digits[-1])
print(total)
