from collections import defaultdict
from typing import Collection, Iterable, Optional, Union

import numpy as np

from .iter import same, only
from .parse import split_lines, drop_prefix, parse_words, parse_ints
