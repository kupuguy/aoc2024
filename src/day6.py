from pathlib import Path
from itertools import cycle

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


def parse(input: str) -> tuple[set[tuple[int, int]], tuple[int, int], int, int]:
    obstacles: set[tuple[int, int]] = set()
    start = (0, 0)
    width, height = 0, 0
    for y, row in enumerate(input.splitlines()):
        width = len(row)
        height = y
        x = -1
        while (x := row.find("#", x + 1)) >= 0:
            obstacles.add((x, y))
        if "^" in row:
            start = (row.find("^"), y)
    return obstacles, start, width, height + 1


DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def part1(input: str) -> int:
    obstacles, start, width, height = parse(input)
    visited: set[tuple[int, int]] = {start}

    print(f"{len(obstacles)} obstacles, {width=}, {height=}, {start=}")
    x, y = start
    for direction in cycle(DIRECTIONS):
        while True:
            nx, ny = x + direction[0], y + direction[1]
            if (nx, ny) in obstacles:
                break
            if 0 <= nx < height and 0 <= ny < width:
                x, y = nx, ny
                visited.add((x, y))
            else:
                return len(visited)


assert part1(TEST) == 41
INPUT = Path("input/day6.txt").read_text()
print(f"{part1(INPUT)=}")  # 5208


def compute_visited(
    obstacles: set[tuple[int, int]], start: tuple[int, int], width: int, height: int
) -> set[int]:
    visited: dict[tuple[int, int], set[tuple[int, int]]] = {start: {DIRECTIONS[0]}}

    x, y = start
    for direction in cycle(DIRECTIONS):
        while True:
            nx, ny = x + direction[0], y + direction[1]
            if (nx, ny) in obstacles:
                break

            if (nx, ny) in visited and direction in visited[nx, ny]:
                return set()  # looping

            if 0 <= nx < height and 0 <= ny < width:
                x, y = nx, ny
                if (x, y) in visited:
                    visited[x, y].add(direction)
                else:
                    visited[x, y] = {direction}
            else:
                return set(visited.keys())


def part2(input: str) -> int:
    obstacles, start, width, height = parse(input)
    visited = compute_visited(obstacles, start, width, height)
    looping: set[tuple[int, int]] = set()
    for p in visited:
        if p == start:
            continue
        if not compute_visited(obstacles | {p}, start, width, height):
            looping.add(p)
    return len(looping)


assert part2(TEST) == 6
print(f"{part2(INPUT)=}")
