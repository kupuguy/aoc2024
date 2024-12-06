from itertools import pairwise
from pathlib import Path

TEST = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".splitlines()


def parse(data: list[str]) -> list[list[int]]:
    return [[int(n) for n in row.split()] for row in data if row]


def is_safe(record: list[int]) -> bool:
    return all(b - a in (1, 2, 3) for a, b in pairwise(record)) or all(
        b - a in (1, 2, 3) for a, b in pairwise(reversed(record))
    )


def part1(data: list[str]) -> int:
    records = parse(data)
    return sum(1 if is_safe(record) else 0 for record in records)


assert part1(TEST) == 2

INPUT = Path("input/day2.txt").read_text().splitlines()
print(part1(INPUT))


def is_safe_damped(record: list[int]) -> bool:
    if is_safe(record):
        return True

    for damped in range(0, len(record)):
        if is_safe(record[:damped] + record[damped + 1 :]):
            return True


def part2(data: list[str]) -> int:
    records = parse(data)
    return sum(1 if is_safe_damped(record) else 0 for record in records)


assert part2(TEST) == 4
print(f"{part2(INPUT)=}")
