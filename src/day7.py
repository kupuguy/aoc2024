from pathlib import Path

TEST = """"""


def parse(input: str) -> tuple[set[complex], complex, int, int]:
    ...

def part1(input: str) -> int:
    ...

assert part1(TEST) == 999
INPUT = Path("input/day7.txt").read_text()
print(f"{part1(INPUT)=}")  #
