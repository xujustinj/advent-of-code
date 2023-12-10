from base import BaseSolution
from util import *


def extrapolate(values: np.ndarray) -> int:
    acc: int = 0
    while not np.all(values == 0):
        acc += values[-1]
        values = values[1:] - values[:-1]
    return int(acc)

class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2023, day=9)

    def part_1_linewise(self, i: int, line: str) -> int:
        return extrapolate(parse_ints(line))

    def part_2_linewise(self, i: int, line: str) -> int:
        return extrapolate(parse_ints(line)[::-1])

Solution()()
