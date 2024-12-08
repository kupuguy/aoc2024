from pathlib import Path

TEST = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def parse(input: str) -> list[tuple[int, list[int]]]:
    parsed: list[tuple[int, list[int]]] = []
    for row in input.splitlines():
        total, _, values = row.partition(":")
        parsed.append((int(total), [int(v) for v in values.strip().split()]))
    return parsed


def can_solve(total: int, values: list[int]) -> bool:
    res = {values[0]}
    for v in values[1:]:
        res = {r + v for r in res} | {r * v for r in res}

    return total in res


def part1(input: str) -> int:
    parsed = parse(input)
    valid = [total for total, values in parsed if can_solve(total, values)]
    return sum(valid)


assert part1(TEST) == 3749

INPUT = Path("input/day7.txt").read_text()
part1_total = part1(INPUT)
print(f"{part1_total=:,}")  # 4,122,618,559,853


def can_solve2(total: int, values: list[int], other: list[int]) -> bool:
    res = {values[0]}
    for v in values[1:]:
        res = (
            {n for r in res if (n := r + v) <= total}
            | {n for r in res if (n := r * v) <= total}
            | {n for r in res if (n := int(str(r) + str(v))) <= total}
        )
    return total in res


def part2(input: str) -> int:
    parsed = parse(input)
    valid = [
        total
        for total, values in parsed
        if can_solve(total, values) or can_solve2(total, values, [])
    ]
    return sum(valid)


assert part2(TEST) == 11387
part2_total = part2(INPUT)
print(f"{part2_total=:,}")  # 227,615,740,238,334
print(part2_total)
