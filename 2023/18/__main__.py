from base import BaseSolution
from util import *


DIRECTIONS = [
    (-1, 0), # U
    ( 0, 1), # R
    ( 1, 0), # D
    ( 0,-1), # L
]

def area(moves: list[tuple[int, int]]):
    i,j = 0,0
    i_set = {i}
    j_set = {j}
    turns = 0
    d: Optional[int] = None
    for dd, ll in moves:
        di, dj = DIRECTIONS[dd]

        i += ll * di
        j += ll * dj
        i_set.add(i)
        j_set.add(j)

        if d is not None:
            if dd == (d + 1) % 4:
                turns += 1
            else:
                assert dd == (d - 1) % 4
                turns -= 1
        d = dd

    assert -4 < turns < 0 or 0 < turns < 4
    t = 1 if turns > 0 else -1

    I = sorted(i_set)
    J = sorted(j_set)
    H = 2*len(I) - 1
    W = 2*len(J) - 1
    grid = np.zeros((H, W), dtype=bool)

    debug(f"Search grid size: {H * W}")

    i, j = 0, 0
    u = I.index(i) * 2
    v = J.index(j) * 2
    grid[u,v] = True
    inside: set[tuple[int, int]] = set()
    for dd, ll in moves:
        di, dj = DIRECTIONS[dd]
        i += ll * di
        j += ll * dj

        ti, tj = DIRECTIONS[(dd + t) % 4]
        inside.add((u + di + ti, v + dj + tj))

        uu = I.index(i) * 2
        vv = J.index(j) * 2
        while True:
            u += di
            v += dj
            grid[u,v] = True
            if (u,v) == (uu,vv):
                break

    acc = 0
    stack = list(inside)
    while len(stack) > 0:
        u,v = stack.pop()
        for (di, dj) in DIRECTIONS:
            uu = u + di
            vv = v + dj
            if uu not in range(H):
                continue
            if vv not in range(W):
                continue
            if grid[uu,vv]:
                continue
            grid[uu,vv] = True
            stack.append((uu,vv))

    for u in range(H):
        for v in range(W):
            if not grid[u,v]:
                continue

            h = 1 if u % 2 == 0 else I[(u+1)//2] - I[(u-1)//2] - 1
            w = 1 if v % 2 == 0 else J[(v+1)//2] - J[(v-1)//2] - 1
            acc += h * w

    return acc


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2023, day=18)

    def part_1(self, lines: list[str]) -> int:
        moves: list[tuple[int, int]] = []
        for line in lines:
            d, l, _ = split(line, seps=" (#)", parse_int=True)
            moves.append(("URDL".index(d), l))
        return area(moves)

    def part_2(self, lines: list[str]) -> int:
        """
        To spite the people who came up with a formula for this,
        here's an alternative solution that still runs in reasonable time.
        """
        moves: list[tuple[int, int]] = []
        for line in lines:
            _, _, color = split(line, seps=" (#)")
            l = int(color[:5], base=16)
            d = int(color[5])
            moves.append((d, l))
        return area(moves)

Solution()()
