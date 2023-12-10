from base import BaseSolution
from util import *

class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=????, day=??)

    def part_1_linewise(self, line: str) -> int:
        return super().part_1_linewise(line)

    def part_1(self, lines: list[str]) -> int:
        return sum(self.part_1_linewise(line) for line in lines)

    def part_2_linewise(self, line: str) -> int:
        return super().part_2_linewise(line)

    def part_2(self, lines: list[str]) -> int:
        return sum(self.part_2_linewise(line) for line in lines)

Solution()()
