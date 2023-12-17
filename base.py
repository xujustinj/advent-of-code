import os
import requests
from typing import Literal, Optional
import time

from termcolor import colored
import pyperclip


def bold(s: str) -> str:
    return colored(s, attrs=("bold",))


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
        assert res.ok, \
            f"Failed to fetch input for {self.__name}. This is expected if the problem has not been released yet."
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

    def part_2_gridwise(self, i: int, block: list[str]) -> int:
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
                    return

                print(bold("\u2500" * 80))
                print(f"    {bold('PART')} \u2502 {part}")

                expect = expect_1 if part == 1 else expect_2

                start_time_s = time.time()
                answer = int((self.part_1 if part == 1 else self.part_2)(in_lines))
                end_time_s = time.time()
                elapsed_ms = (end_time_s - start_time_s) * 1e3

                if answer < 0:
                    print("NOT IMPLEMENTED YET")
                    return

                color: Optional[str] = (
                    None if expect is None else
                    "green" if expect == answer else
                    "red"
                )
                if expect is not None:
                    print(f"{bold('EXPECTED')} \u2502 {expect}")
                out = f"  {bold('ANSWER')} \u2502 {colored(str(answer), color=color)}"

                if copy:
                    try:
                        pyperclip.copy(answer)
                        out += "  \U0001f4cb"
                    except:
                        pass

                print(out)
                print(f"    {bold('TIME')} \u2502 {elapsed_ms:.3f} ms")


            run_part(1)
            try:
                run_part(2)
            except NotImplementedError:
                pass

        print(bold(self.__name))
        for name in input_names:
            print(bold("\u2501" * 80))
            print(f"   {bold('INPUT')} \u2502 {name}")
            run_on_input(name, copy=(name == "input"))
