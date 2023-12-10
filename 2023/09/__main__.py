from base import BaseSolution
from util import *


def extrapolate(values: list[int]) -> int:
    acc: int = 0
    while not all(n == 0 for n in values):
        acc += values[-1]
        values = [r-l for l,r in zip(values[:-1], values[1:])]
    return acc

class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2023, day=9)

    def part_1(self, lines: list[str]) -> int:
        return sum(
            extrapolate(parse_ints(line))
            for line in lines
        )

    def part_2(self, lines: list[str]) -> int:
        return sum(
            extrapolate(list(reversed(parse_ints(line))))
            for line in lines
        )

Solution()()
