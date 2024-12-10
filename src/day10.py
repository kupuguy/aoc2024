from pathlib import Path

TEST = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def parse(input: str) -> dict[complex, int]:
    trailmap: dict[complex, int] = {}
    for y, row in enumerate(input.splitlines()):
        for x, height in enumerate(row):
            trailmap[complex(x, y)] = int(height)
    return trailmap


def part1(input: str) -> int:
    trailmap = parse(input)
    starts = [k for k in trailmap if trailmap[k] == 0]
    score = 0
    for s in starts:
        points = {s}
        for height in range(1, 10):
            points = {
                p
                for q in points
                for p in (q + 1, q - 1, q + 1j, q - 1j)
                if p in trailmap and trailmap[p] == height
            }
        score += len(points)
    return score

assert part1(TEST) == 36

INPUT = Path("input/day10.txt").read_text()
part1_total = part1(INPUT)
print(f"{part1_total=:,}")

def part2(input: str) -> int:
    trailmap = parse(input)
    starts = [k for k in trailmap if trailmap[k] == 0]
    score = 0
    for s in starts:
        points = {s: 1}
        for height in range(1, 10):
            new: dict[complex, int] = {}
            for q in points:
                for p in (q + 1, q - 1, q + 1j, q - 1j):
                    if p in trailmap and trailmap[p] == height:
                        new[p] = new.get(p, 0) + points[q]
            points = new
        score += sum(points.values())
    return score

assert part2(TEST) == 81

part2_total = part2(INPUT)
print(f"{part2_total=:,}")
