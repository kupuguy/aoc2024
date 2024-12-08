from pathlib import Path
from typing import Sequence

TEST = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def parse(input: str) -> Sequence[tuple[str, complex]]:
    for y, row in enumerate(input.splitlines()):
        for x, ch in enumerate(row):
            if ch != ".":
                yield (ch, complex(x, y))


def part1(input: str) -> int:
    antennas: dict[str, list[complex]] = {}
    antinodes: set[complex] = set()
    lines = input.splitlines()
    width = len(lines[0])
    height = len(lines)

    for freq, position in parse(input):
        for other in antennas.setdefault(freq, []):
            for pnode in (
                other + (other - position),
                position + (position - other),
            ):
                if 0 <= pnode.real < width and 0 <= pnode.imag < height:
                    antinodes.add(pnode)

        antennas[freq].append(position)
    return len(antinodes)


assert part1(TEST) == 14

INPUT = Path("input/day8.txt").read_text()
part1_total = part1(INPUT)
print(f"{part1_total=:,}")  # 256


def part2(input: str) -> int:
    antennas: dict[str, list[complex]] = {}
    antinodes: set[complex] = set()
    lines = input.splitlines()
    width = len(lines[0])
    height = len(lines)

    for freq, position in parse(input):
        for other in antennas.setdefault(freq, []):
            for diff, pnode in (other - position, other), (position - other, position):
                while 0 <= pnode.real < width and 0 <= pnode.imag < height:
                    antinodes.add(pnode)
                    pnode += diff

        antennas[freq].append(position)
    return len(antinodes)


assert part2(TEST) == 34
part2_total = part2(INPUT)
print(f"{part2_total=:,}")  #
print(part2_total)
