from base import BaseSolution
from util import *

class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2023, day=2)

    def part_1_linewise(self, i: int, line: str) -> int:
        game, draws = split(line, seps=":")
        id = int(game.removeprefix("Game "))
        for draw in hierarchical_split(draws, seps=";, "):
            for count, color in draw:
                n = int(count)
                if (
                    (color == "red" and n > 12)
                    or (color == "green" and n > 13)
                    or (color == "blue" and n > 14)
                ):
                    return 0
        return id

    def part_1(self, lines: list[str]) -> int:
        answer = sum(self.part_1_linewise(i, line) for i, line in enumerate(lines))
        return answer

    def part_2_linewise(self, i: int, line: str) -> int:
        r: int = 0
        g: int = 0
        b: int = 0
        draws = drop_prefix(line, delimiter=":")
        for draw in hierarchical_split(draws, seps=";, "):
            for count, color in draw:
                n = int(count)
                if color == "red":
                    r = max(r, n)
                elif color == "green":
                    g = max(g, n)
                elif color == "blue":
                    b = max(b, n)
        return r * g * b

    def part_2(self, lines: list[str]) -> int:
        answer = sum(self.part_2_linewise(i, line) for i, line in enumerate(lines))
        return answer

Solution()()
