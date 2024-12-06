from pathlib import Path

TEST = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def parse(input: str) -> tuple[set[complex], complex, int, int]:
    obstacles: set[complex] = set()
    start = 0 + 0j
    width, height = 0, 0
    for y, row in enumerate(input.splitlines()):
        width = len(row)
        height = y
        x = -1
        while (x := row.find("#", x + 1)) >= 0:
            obstacles.add(x + y * 1j)
        if "^" in row:
            start = row.find("^") + y * 1j
    return obstacles, start, width, height + 1


DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def part1(input: str) -> int:
    obstacles, start, width, height = parse(input)
    visited: set[complex] = {start}

    print(f"{len(obstacles)} obstacles, {width=}, {height=}, {start=}")
    pos = start
    direction = -1j
    while True:
        npos = pos + direction
        if npos in obstacles:
            direction *= 1j
        elif 0 <= npos.imag < height and 0 <= npos.real < width:
            pos = npos
            visited.add(pos)
        else:
            return len(visited)


assert part1(TEST) == 41
INPUT = Path("input/day6.txt").read_text()
print(f"{part1(INPUT)=}")  # 5208


def compute_visited(
    obstacles: set[complex], start: complex, width: int, height: int
) -> set[complex]:
    direction = -1j
    visited: set[complex] = {start}
    turns: set[complex] = set()

    pos = start
    while True:
        npos = pos + direction
        if npos in obstacles:
            while npos in obstacles:
                direction *= 1j
                npos = pos + direction
            if pos in turns:
                return set()
            turns.add(pos)

        if 0 <= npos.imag < height and 0 <= npos.real < width:
            pos = npos
            visited.add(pos)
        else:
            return visited


def is_looping(
    obstacles: set[complex], start: complex, width: int, height: int
) -> bool:
    direction = -1j
    turns: set[complex] = set()

    pos = start
    while True:
        npos = pos + direction
        if npos in obstacles:
            while npos in obstacles:
                direction *= 1j
                npos = pos + direction
            if pos in turns:
                return True
            turns.add(pos)

        if 0 <= npos.imag < height and 0 <= npos.real < width:
            pos = npos
        else:
            return False


def part2(input: str) -> int:
    obstacles, start, width, height = parse(input)
    visited = compute_visited(obstacles, start, width, height)
    looping: set[complex] = set()
    for p in visited - {start}:
        if is_looping(obstacles | {p}, start, width, height):
            looping.add(p)
    return len(looping)


assert part2(TEST) == 6
print(f"{part2(INPUT)=}")  # 1972
