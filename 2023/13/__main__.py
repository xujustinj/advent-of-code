from base import BaseSolution
from util import *

def symmetric(grid: np.ndarray, i: int, tol: int = 0) -> bool:
    H, _ = grid.shape
    delta = 0
    for j in range(min(i, H-i)):
        delta += (grid[i+j] != grid[i-j-1]).sum()
        if delta > tol:
            return False
    if delta < tol:
        return False
    return True

class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2023, day=13)

    def part_1_blockwise(self, i: int, block: list[str]) -> int:
        grid, H, W = parse_grid(block)
        for j in range(1, H):
            if symmetric(grid, j):
                return 100 * j
        for j in range(1, W):
            if symmetric(grid.T, j):
                return j

    def part_1(self, lines: list[str]) -> int:
        # answer = 0
        # answer = sum(self.part_1_linewise(i, line) for i, line in enumerate(lines))
        answer = sum(self.part_1_blockwise(i, block) for i, block in enumerate(split_lines(lines)))
        return answer

    def part_2_blockwise(self, i: int, block: list[str]) -> int:
        grid, H, W = parse_grid(block)
        for j in range(1, H):
            if symmetric(grid, j, tol=1):
                return 100 * j
        for j in range(1, W):
            if symmetric(grid.T, j, tol=1):
                return j

    def part_2(self, lines: list[str]) -> int:
        # answer = 0
        # answer = sum(self.part_2_linewise(i, line) for i, line in enumerate(lines))
        answer = sum(self.part_2_blockwise(i, block) for i, block in enumerate(split_lines(lines)))
        return answer

Solution()()
