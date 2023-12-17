from base import BaseSolution
from util import *

def hash(s: str) -> int:
    h = 0
    for c in s:
        h = ((h + ord(c)) * 17) % 256
    return h

class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2023, day=15)

    def part_1(self, lines: list[str]) -> int:
        assert len(lines) == 1
        return sum(hash(s) for s in split(lines[0], seps=","))

    def part_2(self, lines: list[str]) -> int:
        assert len(lines) == 1
        boxes: list[dict[str, int]] = [{} for _ in range(256)]
        for step in split(lines[0], seps=","):
            if step.endswith("-"):
                label = step[:-1]
                boxes[hash(label)].pop(label, None)
            else:
                label, focal_length = split(step, "=")
                boxes[hash(label)][label] = int(focal_length)

        acc: int = 0
        for b, box in enumerate(boxes):
            for i, f in enumerate(box.values()):
                acc += (b+1) * (i+1) * f
        return acc


Solution()()
