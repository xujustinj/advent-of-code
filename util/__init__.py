from collections import defaultdict
import heapq
import math
import re
from typing import (
    Collection,
    Iterable,
    Literal,
    Optional,
    Sequence,
    Union,
)

import numpy as np

from .debug import debug, debug_grid
from .iter import same, only
from .parse import (
    split_lines,
    split,
    drop_prefix,
    hierarchical_split,
    parse_ints,
    parse_grid,
)
from .int_range import Range
