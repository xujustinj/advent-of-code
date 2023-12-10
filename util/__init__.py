from collections import defaultdict
import math
import re
from typing import (
    Collection,
    Iterable,
    Optional,
    Sequence,
    Union,
)

import numpy as np

from .iter import same, only
from .parse import (
    split_lines,
    split,
    drop_prefix,
    hierarchical_split,
    parse_ints,
)
