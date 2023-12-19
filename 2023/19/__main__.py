from base import BaseSolution
from typing import TypeAlias
from util import *

Rule: TypeAlias = tuple[int, str, int, str]
Workflow: TypeAlias = tuple[list[Rule], str]
Part: TypeAlias = tuple[int, int, int, int]
PartRange: TypeAlias = tuple[Range, Range, Range, Range]

def parse_rule(s: str) -> Rule:
    var = "xmas".index(s[0])

    cond = s[1]
    assert cond in "<>"

    val, to = split(s[2:], ":", parse_int=True)
    assert isinstance(val, int)

    return var, cond, val, to

def parse_workflow(s: str) -> tuple[str, Workflow]:
    name, rest = split(s, seps="{}")
    tokens = split(rest, seps=",")
    rules = ([parse_rule(t) for t in tokens[:-1]], tokens[-1])
    return name, rules

def parse_part(s: str) -> tuple[int, int, int, int]:
    return tuple(int(t[2:]) for t in split(s, seps="{,}"))

class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2023, day=19)

    def part_1(self, lines: list[str]) -> int:
        workflows_lines, parts_lines = split_lines(lines)
        workflows = dict(parse_workflow(line) for line in workflows_lines)
        parts: list[tuple[Part, str]] = [(parse_part(line), "in") for line in parts_lines]

        acc: int = 0
        while len(parts) > 0:
            part, name = parts.pop()

            if name == "R":
                continue

            if name == "A":
                acc += sum(part)
                continue

            rules, rest = workflows[name]
            for var, cond, val, to in rules:
                actual = part[var]
                ok = {">": actual > val, "<": actual < val}[cond]
                if ok:
                    parts.append((part, to))
                    break
            else:
                parts.append((part, rest))

        return acc

    def part_2(self, lines: list[str]) -> int:
        workflows_lines, _ = split_lines(lines)
        workflows = dict(parse_workflow(line) for line in workflows_lines)

        r = Range.cc(1,4000)
        parts: list[tuple[PartRange, str]] = [((r,r,r,r), "in")]
        acc: int = 0
        while len(parts) > 0:
            part, name = parts.pop()

            if any(r.is_empty for r in part):
                continue

            if name == "R":
                continue

            if name == "A":
                n: int = 1
                for r in part:
                    n *= len(r)
                acc += n
                continue

            rules, rest = workflows[name]
            for var, cond, val, to in rules:
                if_cond = {">": dict(lex=val), "<": dict(rex=val)}[cond]
                ok = tuple(
                    r.clip(**if_cond) if i == var else r
                    for i, r in enumerate(part)
                )
                parts.append((ok, to))

                else_cond = {">": dict(rin=val), "<": dict(lin=val)}[cond]
                part = tuple(
                    r.clip(**else_cond) if i == var else r
                    for i, r in enumerate(part)
                )
            parts.append((part, rest))

        return acc

Solution()()
