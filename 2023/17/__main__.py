from base import BaseSolution
from util import *


DIRECTIONS = ((-1,0), (0,1), (1,0), (0,-1))

class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2023, day=17)

    def part_1(self, lines: list[str]) -> int:
        grid, H, W = parse_grid(lines)
        distance: dict[tuple[int,int], int] = dict()
        paths: set[tuple[int,int,int,Optional[int],int]] = set()
        queue: list[tuple[int,int,int,Optional[int],int]] = [(0,0,0,None,0)]
        while (H-1, W-1) not in distance:
            w,i,j,d,m = heapq.heappop(queue)

            if (i,j,d,m) in paths:
                continue
            paths.add((i,j,d,m))

            if (i,j) in distance:
                assert distance[(i,j)] <= w
            else:
                distance[(i,j)] = w

            for dd, (di, dj) in enumerate(DIRECTIONS):
                if d is not None and dd == (d+2) % 4:
                    continue
                mm = m+1 if dd == d else 1
                if mm > 3:
                    assert dd == d
                    continue

                ii = i + di
                if ii not in range(H):
                    continue
                jj = j + dj
                if jj not in range(W):
                    continue

                if (ii, jj, dd, mm) in paths:
                    continue

                ww = w + grid[ii,jj]
                heapq.heappush(queue, (ww, ii, jj, dd, mm))

        debug(f"Solution found after searching {len(paths)} squares.")
        return distance[(H-1, W-1)]

    def part_2(self, lines: list[str]) -> int:
        grid, H, W = parse_grid(lines)
        distance: dict[tuple[int,int], int] = dict()
        paths: set[tuple[int,int,int,Optional[int],int]] = set()
        queue: list[tuple[int,int,int,Optional[int],int]] = [(0,0,0,None,0)]
        while (H-1, W-1) not in distance:
            w,i,j,d,m = heapq.heappop(queue)

            if (i,j,d,m) in paths:
                continue
            paths.add((i,j,d,m))

            if (i,j) in distance:
                assert distance[(i,j)] <= w
            else:
                distance[(i,j)] = w

            for dd, (di, dj) in enumerate(DIRECTIONS):
                if d is not None and dd == (d+2) % 4:
                    continue
                if d is not None and m < 4 and dd != d:
                    continue
                mm = m+1 if dd == d else 1
                if mm > 10:
                    assert dd == d
                    continue

                ii = i + di
                if ii not in range(H):
                    continue
                jj = j + dj
                if jj not in range(W):
                    continue

                if (ii, jj, dd, mm) in paths:
                    continue

                ww = w + grid[ii,jj]
                heapq.heappush(queue, (ww, ii, jj, dd, mm))

        debug(f"Solution found after searching {len(paths)} squares.")
        return distance[(H-1, W-1)]

Solution()()
