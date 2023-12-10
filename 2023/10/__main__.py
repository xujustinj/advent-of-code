from collections import defaultdict
import re

from base import BaseSolution

class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2023, day=10)

    def part_1(self, lines: list[str]) -> int:
        adjacent: dict[tuple[int, int], list[tuple[int, int]]] = {}
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c == "|":
                    adjacent[(i,j)] = [(i-1,j), (i+1,j)]
                elif c == "-":
                    adjacent[(i,j)] = [(i,j-1), (i,j+1)]
                elif c == "L":
                    adjacent[(i,j)] = [(i-1,j), (i,j+1)]
                elif c == "J":
                    adjacent[(i,j)] = [(i-1,j), (i,j-1)]
                elif c == "7":
                    adjacent[(i,j)] = [(i+1,j), (i,j-1)]
                elif c == "F":
                    adjacent[(i,j)] = [(i+1,j), (i,j+1)]
                if c == "S":
                    s = (i,j)
                    adjacent[(i,j)] = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]

        queue = [s]
        depth: dict[tuple[int, int], int] = {s: 0}
        while len(queue) > 0:
            x = queue.pop(0)
            for y in adjacent[x]:
                if y in adjacent and x in adjacent[y] and y not in depth:
                        depth[y] = depth[x] + 1
                        queue.append(y)

        return max(depth.values())

    def part_2(self, lines: list[str]) -> int:
        H = len(lines)
        W = len(lines[0])

        adjacent: dict[tuple[int, int], list[tuple[int, int]]] = {}
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c == "|":
                    a = [(i-1,j), (i+1,j)]
                elif c == "-":
                    a = [(i,j-1), (i,j+1)]
                elif c == "L":
                    a = [(i-1,j), (i,j+1)]
                elif c == "J":
                    a = [(i-1,j), (i,j-1)]
                elif c == "7":
                    a = [(i+1,j), (i,j-1)]
                elif c == "F":
                    a = [(i+1,j), (i,j+1)]
                elif c == "S":
                    s = (i,j)
                    a = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
                else:
                    continue
                adjacent[(i,j)] = a

        lefts: set[tuple[int, int]] = set()
        parent: dict[tuple[int, int], tuple[int, int] | None] = {s: None}
        x = s
        while True:
            ys = [
                y for y in adjacent[x]
                if y in adjacent and x in adjacent[y] and y != parent[x]
            ]
            assert len(ys) == (2 if x == s else 1), ys
            y = ys[0]

            d = (y[1]-x[1], x[0]-y[0]) # "left" vector

            for l in ((x[0]+d[0], x[1]+d[1]), (y[0]+d[0], y[1]+d[1])):
                if l[0] in range(H) and l[1] in range(W):
                    lefts.add(l)

            parent[y] = x
            if y == s:
                break
            x = y

        loop = set(parent.keys())
        lefts = lefts - loop

        queue = list(lefts)
        while len(queue) > 0:
            i,j = queue.pop(0)
            for ii,jj in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
                if ii in range(H) and jj in range(W):
                    if (ii,jj) not in loop and (ii,jj) not in lefts:
                        lefts.add((ii,jj))
                        queue.append((ii,jj))

        out = any((i == 0 or j == 0 or i == H-1 or j == W-1) for i,j in lefts)
        if out:
            return H * W - len(loop) - len(lefts)
        else:
            return len(lefts)

Solution()()
