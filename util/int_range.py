from typing import Iterator, Optional, Union

class Range:
    """
    An integer range.
    By default, this follows the left-inclusive, right-exclusive semantics of
     Python's built-in range class.
        Range(a,b) = [a,b)

    The preferred way to construct a Range is using the class methods:
        Range.oo(a,b) = (a,b)
        Range.oc(a,b) = (a,b]
        Range.co(a,b) = [a,b)
        Range.cc(a,b) = [a,b]
    """
    def __init__(
            self,
            *bounds: int,
            lex: Optional[int] = None,
            lin: Optional[int] = None,
            rin: Optional[int] = None,
            rex: Optional[int] = None,
    ):
        if len(bounds) > 0:
            assert lex is None
            assert lin is None
            assert rin is None
            assert rex is None
            lin, rex = bounds
        else:
            if lin is None:
                assert lex is not None
                lin = lex + 1
            else:
                assert lex is None

            if rex is None:
                assert rin is not None
                rex = rin + 1
            else:
                assert rin is None

        self.range = range(lin, rex)

    @classmethod
    def oo(cls, lex: int, rex: int) -> "Range":
        """
        open-open (lex,rex)
        """
        return cls(lex=lex, rex=rex)

    @classmethod
    def oc(cls, lex: int, rin: int) -> "Range":
        """
        open-closed (lex,rin]
        """
        return cls(lex=lex, rin=rin)

    @classmethod
    def co(cls, lin: int, rex: int) -> "Range":
        """
        closed-open [lin,rex)
        """
        return cls(lin=lin, rex=rex)

    @classmethod
    def cc(cls, lin: int, rin: int) -> "Range":
        """
        closed-closed [lin,rin]
        """
        return cls(lin=lin, rin=rin)

    @classmethod
    def empty(cls) -> "Range":
        return cls.co(lin=0, rex=0)

    @property
    def lin(self) -> int:
        return self.range.start

    @property
    def lex(self) -> int:
        return self.lin - 1

    @property
    def rin(self) -> int:
        return self.rex - 1

    @property
    def rex(self) -> int:
        return self.range.stop

    def __iter__(self) -> Iterator[int]:
        return iter(self.range)

    def __len__(self) -> int:
        return len(self.range)

    @property
    def is_empty(self) -> bool:
        return len(self) <= 0

    def __add__(self, other: Union[int, "Range"]) -> "Range":
        """
        { x + y | x in self and y in other }
        """
        assert isinstance(other, (int, Range))

        if isinstance(other, int):
            return Range(
                lin=self.lin+other,
                rex=self.rex+other,
            )

        if self.is_empty or other.is_empty:
            return Range.empty()

        return Range.cc(
            lin=(self.lin + other.lin),
            rin=(self.rin + other.rin),
        )

    def __neg__(self) -> "Range":
        """
        { -x | x in self }
        """
        return Range.cc(
            lin=-self.rin,
            rin=-self.lin,
        )

    def clip(
            self,
            lin: Optional[int] = None,
            lex: Optional[int] = None,
            rin: Optional[int] = None,
            rex: Optional[int] = None,
    ) -> "Range":
        assert (lin is None) or (lex is None)
        assert (rin is None) or (rex is None)

        if lex is not None:
            lin = lex + 1
        if lin is not None:
            lin = max(lin, self.lin)
        else:
            lin = self.lin

        if rin is not None:
            rex = rin + 1
        if rex is not None:
            rex = min(rex, self.rex)
        else:
            rex = self.rex

        return Range.co(lin=lin, rex=rex)

    def __contains__(self, x: int) -> bool:
        return x in self.range

    def __repr__(self) -> str:
        if self.is_empty:
            return "[]"
        return f"[{self.lin},{self.rex})"
