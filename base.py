import os
import requests
from typing import Literal, Optional

import pyperclip


class BaseSolution:
    __SESSION_PATH = "session"
    __INPUT_EXT = ".in.txt"

    def __init__(self, year: int, day: int):
        self.year = year
        self.day = day

    @property
    def __name(self) -> str:
        return f"{self.year} Advent of Code #{self.day}"

    @property
    def __base_path(self) -> str:
        return f"{self.year}/{self.day:02d}"

    @property
    def __input_cache_path(self) -> str:
        basename = f"input{BaseSolution.__INPUT_EXT}"
        return os.path.join(self.__base_path, basename)

    @property
    def __input_url(self) -> str:
        return f"https://adventofcode.com/{self.year}/day/{self.day}/input"

    @property
    def __session_cookie(self) -> str:
        with open(self.__SESSION_PATH) as f:
            return f.read()

    def __get_input(self):
        if os.path.exists(self.__input_cache_path):
            return

        cookies = dict(session=self.__session_cookie)
        res = requests.get(self.__input_url, cookies=cookies)
        assert res.ok
        text = res.text

        os.makedirs(os.path.dirname(self.__input_cache_path), exist_ok=True)
        with open(self.__input_cache_path, "w") as f:
            f.write(text)

    def part_1_linewise(self, i: int, line: str) -> int:
        raise NotImplementedError(
            f"{self.__name} Part 1 has not been implemented yet."
        )

    def part_1_blockwise(self, i: int, block: list[str]) -> int:
        raise NotImplementedError(
            f"{self.__name} Part 1 has not been implemented yet."
        )

    def part_1(self, lines: list[str]) -> int:
        raise NotImplementedError(
            f"{self.__name} Part 1 has not been implemented yet."
        )

    def part_2_linewise(self, i: int, line: str) -> int:
        raise NotImplementedError(
            f"{self.__name} Part 2 has not been implemented yet."
        )

    def part_2_blockwise(self, i: int, block: list[str]) -> int:
        raise NotImplementedError(
            f"{self.__name} Part 2 has not been implemented yet."
        )

    def part_2(self, lines: list[str]) -> int:
        raise NotImplementedError(
            f"{self.__name} Part 2 has not been implemented yet."
        )

    def __call__(self):
        self.__get_input()

        names: set[str] = set()
        for basename in os.listdir(self.__base_path):
            if basename.endswith(".in.txt"):
                name = basename.removesuffix(self.__INPUT_EXT)
                names.add(name)

        # make sure to run on the main input last
        assert "input" in names
        names.remove("input")

        input_names = sorted(names) + ["input"]

        def run_on_input(name: str, copy: bool):
            input_path = os.path.join(self.__base_path, f"{name}.in.txt")
            with open(input_path) as f:
                in_lines = f.read().splitlines()

            output_path = os.path.join(self.__base_path, f"{name}.out.txt")
            error_1: bool = False
            error_2: bool = False
            expect_1: Optional[int] = None
            expect_2: Optional[int] = None
            if os.path.exists(output_path):
                with open(output_path) as f:
                    out_lines = f.read().splitlines()
                if out_lines[0] == "-":
                    error_1 = True
                elif out_lines[0] != "*":
                    expect_1 = int(out_lines[0])
                if out_lines[1] == "-":
                    error_2 = True
                elif out_lines[1] != "*":
                    expect_2 = int(out_lines[1])

            def run_part(part: Literal[1,2]):
                error = error_1 if part == 1 else error_2
                if error:
                    print(f" part {part}: ---")
                    return
                expect = expect_1 if part == 1 else expect_2
                answer = (self.part_1 if part == 1 else self.part_2)(in_lines)
                if expect is None:
                    print(f" part {part}: {answer}")
                elif expect == answer:
                    print(f" part {part}: {answer}  \u2705")
                else:
                    print(f" part {part}: {answer}  \u274c {expect}")
                if copy:
                    pyperclip.copy(answer)

            run_part(1)
            try:
                run_part(2)
            except NotImplementedError:
                pass

        print(self.__name)
        for name in input_names:
            print("-" * 80)
            print(f"INPUT: {name}")
            run_on_input(name, copy=(name == "input"))
