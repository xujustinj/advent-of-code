from base import BaseSolution
from util import *

class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=????, day=??)

    def part_1_linewise(self, i: int, line: str) -> int:
        return super().part_1_linewise(i, line)

    def part_1_blockwise(self, i: int, block: list[str]) -> int:
        return super().part_1_blockwise(i, block)

    def part_1(self, lines: list[str]) -> int:
        answer = 0
        # answer = sum(self.part_1_linewise(i, line) for i, line in enumerate(lines))
        # answer = sum(self.part_1_blockwise(i, block) for i, block in enumerate(split_lines(lines)))
        return answer

    def part_2_linewise(self, i: int, line: str) -> int:
        return super().part_2_linewise(i, line)

    def part_2_blockwise(self, i: int, block: list[str]) -> int:
        return super().part_2_blockwise(i, block)

    def part_2(self, lines: list[str]) -> int:
        answer = 0
        # answer = sum(self.part_2_linewise(i, line) for i, line in enumerate(lines))
        # answer = sum(self.part_2_blockwise(i, block) for i, block in enumerate(split_lines(lines)))
        return answer

Solution()()
