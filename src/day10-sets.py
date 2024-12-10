from pathlib import Path
from collections import defaultdict

TEST = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def parse(input: str) -> list[set[complex]]:
    trailmap: dict[complex, int] = {
        complex(x, y): int(height)
        for y, row in enumerate(input.splitlines())
        for x, height in enumerate(row)
    }
    return [{p for p in trailmap if trailmap[p] == height} for height in range(0, 10)]


def part1(input: str) -> int:
    heights = parse(input)
    score = 0
    for s in heights[0]:
        points = {s}
        for level in heights[1:]:
            points = {q + offset for q in points for offset in (1, -1, 1j, -1j)} & level
        score += len(points)
    return score


assert part1(TEST) == 36

INPUT = Path("input/day10.txt").read_text()
part1_total = part1(INPUT)
print(f"{part1_total=:,}")

def part2(input: str) -> int:
    heights = parse(input)
    score = 0
    for s in heights[0]:
        points = {s: 1}
        for level in heights[1:]:
            new: dict[complex, int] = defaultdict(int)
            for q in points:
                for p in {q + 1, q - 1, q + 1j, q - 1j} & level:
                    new[p] += points[q]
            points = new
        score += sum(points.values())
    return score


assert part2(TEST) == 81

part2_total = part2(INPUT)
print(f"{part2_total=:,}")
