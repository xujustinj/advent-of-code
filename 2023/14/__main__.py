from base import BaseSolution
from util import *

def weigh(
        grid: np.ndarray,
        direction: Literal["N","W","S","E"] = "N",
) -> tuple[np.ndarray, int]:
    if direction == "N":
        return weigh(grid.T, direction="W")
    if direction == "S":
        return weigh(grid[::-1,:], direction="N")
    if direction == "E":
        return weigh(grid[:,::-1], direction="W")

    H, W = grid.shape
    weight: int = 0
    for j in np.nonzero(grid == "O")[1]:
        weight += W - int(j)
    return weight

def slide(
        grid: np.ndarray,
        direction: Literal["N","W","S","E"] = "N",
) -> tuple[np.ndarray, int]:
    if direction == "N":
        slid, weight = slide(grid.T, direction="W")
        return slid.T, weight
    if direction == "S":
        slid, weight = slide(grid[::-1,:], direction="N")
        return slid[::-1,:], weight
    if direction == "E":
        slid, weight = slide(grid[:,::-1], direction="W")
        return slid[:,::-1], weight
    assert direction == "W"

    H, W = grid.shape
    grid = np.copy(grid)
    weight: int = 0
    for row in grid:
        cursor: int = 0
        for i in range(W):
            if row[i] == "#":
                cursor = i+1
            elif row[i] == "O":
                row[i] = "."
                row[cursor] = "O"
                weight += (W - cursor)
                cursor += 1
    return grid, weight

class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2023, day=14)

    def part_1(self, lines: list[str]) -> int:
        grid, _, _ = parse_grid(lines)
        _, answer = slide(grid)
        return answer

    def part_2(self, lines: list[str]) -> int:
        N = 1_000_000_000
        grid, H, W = parse_grid(lines)
        past_grids = [grid]
        for c in range(1, N+1):
            for direction in "NWSE":
                grid, _ = slide(grid, direction)

            past_grids.append(grid)
            for i, past in enumerate(past_grids[:-1]):
                if (past == grid).all():
                    r = N - c
                    l = c - i
                    debug(f"Grid is same after {i} and {c} cycles (length {l}).")
                    b = int(math.ceil(r / l)) * l
                    f = N - b
                    assert i < f <= c
                    debug(f"Final grid after {N} cycles is equivalent to grid after {f} cycles (look back {b} cycles).")
                    final = past_grids[f]
                    # debug_grid(final, prefix="\t")
                    return weigh(final)

        return weigh(grid)

Solution()()
