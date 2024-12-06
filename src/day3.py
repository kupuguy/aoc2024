from pathlib import Path
from typing import Sequence
import re

TEST = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""


def parse(input: str) -> Sequence[tuple[int, int]]:
    values = [(int(a), int(b)) for a, b in re.findall(r"mul\((\d+),(\d+)\)", input)]

    # print(values)
    return values


def part1(input: str) -> int:
    return sum(a * b for a, b in parse(input))


assert part1(TEST) == 161

INPUT = Path("input/day3.txt").read_text()
print(f"{part1(INPUT)=}")  # 192767529

TEST2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


def parse2(input: str) -> Sequence[tuple[int, int]]:
    matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", input)
    # print(matches)
    values: list[tuple[int, int]] = []
    working = True
    for a, b, is_do, is_dont in matches:
        if is_do:
            working = True
            continue
        elif is_dont:
            working = False
            continue
        elif working:
            values.append((int(a), int(b)))

    # print(values)
    return values


def part2(input: str) -> int:
    return sum(a * b for a, b in parse2(input))


assert part2(TEST2) == 48
print(f"{part2(INPUT)=}")  # 104083373
