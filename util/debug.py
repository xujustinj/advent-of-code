from typing import Any

import numpy as np


def debug(x: Any, prefix: str = ""):
    s = str(x)
    for line in s.splitlines():
        print(prefix + line)


def debug_grid(grid: np.ndarray, prefix: str = ""):
    s = "\n".join("".join(row) for row in grid)
    debug(s, prefix)
