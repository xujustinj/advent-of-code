import sys
from typing import Any

from termcolor import colored

import numpy as np


def debug(
        x: Any,
        prefix: str = "         > ",
        color: str = "blue",
        color_prefix: bool = False,
        exit_after: bool = False,
        **kwargs,
):
    s = str(x)
    for line in s.splitlines():
        if color_prefix:
            out = colored(prefix + line, color=color, **kwargs)
        else:
            out = prefix + colored(line, color=color, **kwargs)
        print(out, file=sys.stderr)
    if exit_after:
        exit(1)


def debug_grid(grid: np.ndarray, prefix: str = ""):
    s = "\n".join("".join(row) for row in grid)
    debug(s, prefix)
