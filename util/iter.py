from typing import Iterable, TypeVar, Union


T = TypeVar("T")

def only(x: Iterable[T]) -> T:
    first, = x
    return first

def same(x: Iterable[T]) -> T:
    it = iter(x)
    first = next(it)
    for rest in it:
        assert rest == first
    return first
