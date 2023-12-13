from base import BaseSolution
from util import *


ways_memo = {} # use this or else there will be EXTREME PAIN AND SUFFERING
def ways(seq: str, sizes: tuple[int]) -> int:
    assert len(sizes) > 0
    min_size = sum(sizes) + len(sizes) - 1
    if len(seq) < min_size:
        return 0
    size = sizes[0]

    if (seq, sizes) in ways_memo:
        return ways_memo[(seq, sizes)]

    acc: int = 0
    for i in range(len(seq) - min_size + 1):
        if "." not in seq[i:i+size]:
            if (
                len(sizes) > 1
                and len(seq) > i + size
                and seq[i+size] != "#"
            ):
                acc += ways(seq[i+size+1:],sizes[1:])
            elif (
                len(sizes) == 1
                and "#" not in seq[i+size:]
            ):
                acc += 1

        if seq[i] == "#":
            break

    ways_memo[(seq, sizes)] = acc
    return acc


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2023, day=12)

    def part_1_linewise(self, i: int, line: str) -> int:
        seq, target = split(line, seps=[" "])
        sizes = tuple(parse_ints(target, seps=[","]))
        return ways(seq, sizes)

    def part_1(self, lines: list[str]) -> int:
        return sum(
            self.part_1_linewise(i, line)
            for i, line in enumerate(lines)
        )

    def part_2_linewise(self, i: int, line: str) -> int:
        seq, target = split(line, seps=[" "])
        sizes = tuple(parse_ints(target, seps=[","]))
        return ways("?".join((seq,) * 5), sizes * 5)

    def part_2(self, lines: list[str]) -> int:
        return sum(
            self.part_2_linewise(i, line)
            for i, line in enumerate(lines)
        )

Solution()()
