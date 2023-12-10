from base import BaseSolution
from util import *

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

class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2023, day=1)

    def part_1_linewise(self, line: str) -> int:
        digits = [c for c in line if c.isnumeric()]
        return int(digits[0] + digits[-1])

    def part_2_linewise(self, line: str) -> int:
        digits: list[str] = digit_re.findall(line)
        return 10 * parse(digits[0]) + parse(digits[-1])

Solution()()
