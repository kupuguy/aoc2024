from pathlib import Path
from collections import Counter

TEST = """3   4
4   3
2   5
1   3
3   9
3   3"""


def parse(data: list[str]) -> tuple[list[int], list[int]]:
    a: list[int] = []
    b: list[int] = []

    for row in data:
        if not row:
            continue
        left, right = row.strip().split()
        a.append(int(left))
        b.append(int(right))
    return a, b


def part1(data: list[str]) -> int:
    a, b = parse(data)
    res = sum(abs(right - left) for left, right in zip(sorted(a), sorted(b)))
    return res


assert part1(TEST.splitlines()) == 11

INPUT = Path("input/day1.txt").read_text().splitlines()
print(part1(INPUT))


def part2(data: list[str]) -> int:
    a, b = parse(data)

    counts = Counter(b)
    return sum(left * counts.get(left, 0) for left in a)


assert part2(TEST.splitlines()) == 31
print(part2(INPUT))
