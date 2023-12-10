from typing import Union

from .iter import only


def split_lines(lines: list[str]) -> tuple[Union[str, list[str]]]:
    buckets: list[list[str]] = [[]]
    for line in lines:
        line = line.strip()
        if len(line.strip()) == 0:
            buckets.append([])
        else:
            buckets[-1].append(line)

    return tuple(
        only(bucket) if len(bucket) == 0 else bucket
        for bucket in buckets
    )

def drop_prefix(line: str, delimiter: str = ":") -> str:
    _, rest = line.split(delimiter, maxsplit=1)
    return rest.strip()

def parse_words(line: str) -> list[int]:
    return [s for s in line.strip().split() if len(s) > 0]

def parse_ints(line: str) -> list[int]:
    return [int(s) for s in parse_words(line)]
