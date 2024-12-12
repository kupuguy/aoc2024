from pathlib import Path

TEST = """125 17"""


def part1(input: str) -> int:
    ...

assert part1(TEST) == 22

INPUT = Path("input/day12.txt").read_text()
part1_total = part1(INPUT)
print(f"{part1_total=:,}")
