import re
from typing import Optional, Sequence, Union

import numpy as np

from .iter import only


def split_lines(lines: Sequence[str]) -> tuple[Union[str, list[str]]]:
    buckets: list[list[str]] = [[]]
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            buckets.append([])
        else:
            buckets[-1].append(line)

    return tuple(
        only(bucket) if len(bucket) == 1 else bucket
        for bucket in buckets
        if len(bucket) > 0
    )

def split(
        line: str,
        seps: Optional[Sequence[str]] = None,
        maxsplit: int = 0,
        parse_int: bool = False,
        parse_float: bool = False,
) -> list[Union[str, int, float]]:
    def parse(token: str) -> Union[str, int, float]:
        if parse_int:
            try:
                return int(token)
            except:
                pass
        if parse_float:
            try:
                return float(token)
            except:
                pass
        return token

    if maxsplit < 0:
        maxsplit = 0
    pattern = (
        r"\s|," if seps is None
        else "|".join(re.escape(sep) for sep in seps)
    )
    return [
        parse(s.strip())
        for s in re.split(pattern, line.strip(), maxsplit=maxsplit)
        if len(s.strip()) > 0
    ]


def drop_prefix(line: str, delimiter: str = ":") -> str:
    _, rest = split(line, seps=[delimiter], maxsplit=1)
    return rest

def hierarchical_split(
        line: str,
        seps: Sequence[Sequence[str]],
) -> list:
    if len(seps) == 0:
        return line.strip()
    return [
        hierarchical_split(line=s.strip(), seps=seps[1:])
        for s in split(line, seps=[seps[0]])
    ]

def parse_ints(line: str, seps: Optional[Sequence[str]] = None) -> np.ndarray:
    return np.array([int(s) for s in split(line, seps=seps, parse_int=True)])

def parse_grid(lines: list[str]) -> tuple[np.ndarray, int, int]:
    try:
        grid = np.array([[int(c) for c in line] for line in lines], dtype=np.int8)
    except:
        grid = np.array([list(line) for line in lines])
    return (grid, *grid.shape)
