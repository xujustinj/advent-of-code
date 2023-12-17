from base import BaseSolution
from util import *


def energized(grid: np.ndarray, i: int = 0, j: int = 0, d: int = 1) -> int:
    DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1)) # N E S W
    TRANSITION = {
        ".": ((0,), (1,), (2,), (3,)),
        "-": ((1,3), (1,), (1,3), (3,)),
        "|": ((0,), (0,2), (2,), (0,2)),
        "\\": ((3,), (2,), (1,), (0,)),
        "/": ((1,), (0,), (3,), (2,)),
    }

    H, W = grid.shape
    illuminated = np.zeros((H, W, len(DIRECTIONS)), dtype=bool)
    illuminated[(i,j,d)] = True
    beams: list[tuple[int, int, int]] = [(i,j,d)]
    while len(beams) > 0:
        i, j, d = beams.pop()
        for dd in TRANSITION[grid[i,j]][d]:
            di, dj = DIRECTIONS[dd]
            ii = i + di
            if ii not in range(H):
                continue
            jj = j + dj
            if jj not in range(W):
                continue
            if not illuminated[ii,jj,dd]:
                illuminated[ii,jj,dd] = True
                beams.append((ii,jj,dd))

    return int(illuminated.any(axis=2).sum())


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2023, day=16)

    def part_1(self, lines: list[str]) -> int:
        grid, H, W = parse_grid(lines)
        return energized(grid)

    def part_2(self, lines: list[str]) -> int:
        grid, H, W = parse_grid(lines)
        acc: int = 0
        for i in range(H):
            acc = max(acc, energized(grid, i, 0, 1))
            acc = max(acc, energized(grid, i, W-1, 3))
        for j in range(W):
            acc = max(acc, energized(grid, 0, j, 2))
            acc = max(acc, energized(grid, H-1, j, 0))
        return acc

Solution()()
