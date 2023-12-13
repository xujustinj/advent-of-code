from base import BaseSolution
from util import *

def answer(lines: list[str], expansion: int) -> int:
    H = len(lines)
    W = len(lines[0])

    row_cost = np.full((H,), fill_value=expansion, dtype=int)
    col_cost = np.full((W,), fill_value=expansion, dtype=int)
    stars = list()
    for i in range(H):
        for j in range(W):
            if lines[i][j] == "#":
                stars.append((i,j))
                row_cost[i] = 1
                col_cost[j] = 1
    row_idx = np.cumsum(row_cost)
    col_idx = np.cumsum(col_cost)

    acc = 0
    stars = [
        np.array([row_idx[s[0]], col_idx[s[1]]], dtype=int)
        for s in stars
    ]
    for s in stars:
        for t in stars:
            if t is not s:
                acc += np.abs(t - s).sum()

    assert acc % 2 == 0
    return int(acc / 2)

class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2023, day=11)

    def part_1(self, lines: list[str]) -> int:
        return answer(lines, expansion=2)

    def part_2(self, lines: list[str]) -> int:
        return answer(lines, expansion=1000000)

Solution()()
