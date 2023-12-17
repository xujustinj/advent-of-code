import sys
from typing import Any

from termcolor import colored

import numpy as np


def debug(
        x: Any,
        prefix: str = "\t",
        color: str = "blue",
        exit_after: bool = False,
        **kwargs,
):
    s = str(x)
    for line in s.splitlines():
        print(
            colored(prefix + line, color=color, **kwargs),
            file=sys.stderr,
        )
    if exit_after:
        exit(1)


def debug_grid(grid: np.ndarray, prefix: str = ""):
    s = "\n".join("".join(row) for row in grid)
    debug(s, prefix)
