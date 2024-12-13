from pathlib import Path
import re
from typing import Sequence


TEST = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def parse(
    input: str,
) -> Sequence[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]:
    values = [int(n) for n in re.findall(r"\d+", input, re.MULTILINE)]
    while values:
        yield (values[0], values[1]), (values[2], values[3]), (values[4], values[5])
        del values[:6]


def solve(a: tuple[int, int], b: tuple[int, int], prize: [int, int]) -> int:
    a_x, a_y = a
    b_x, b_y = b
    prize_x, prize_y = prize
    cost = 999
    for b_press in range(1, 101):
        res_x = prize_x - (b_press * b_x)
        res_y = prize_y - (b_press * b_y)
        if res_x < 0 or res_y < 0:
            break
        if res_x % a_x == 0:
            press_a = res_x // a_x
            if a_y * press_a == res_y:
                cost = min(3 * press_a + b_press, cost)
    return 0 if cost == 999 else cost


def part1(input: str) -> int:
    return sum(solve(a, b, prize) for a, b, prize in parse(input))


assert part1(TEST) == 480

INPUT = Path("input/day13.txt").read_text()
part1_total = part1(INPUT)
print(f"{part1_total=:,}")  # 34,393

ERROR = 10_000_000_000_000


def solve_2(
    a: tuple[int, int], b: tuple[int, int], prize: [int, int], error: int
) -> int:
    a_x, a_y = a
    b_x, b_y = b
    prize_x, prize_y = prize[0] + error, prize[1] + error

    num = a_x * b_x * prize_y - a_y * b_x * prize_x
    denom = a_x * b_y - a_y * b_x
    x_intersect = num // denom
    press_b = x_intersect // b_x
    press_a = (prize_x - x_intersect) // a_x
    if (
        press_a >= 0
        and press_b >= 0
        and a_y * press_a + b_y * press_b == prize_y
        and a_x * press_a + b_x * press_b == prize_x
    ):
        return press_b + 3 * press_a
    return 0


def part2(input: str, error: int = ERROR) -> int:
    return sum(solve_2(a, b, prize, error=error) for a, b, prize in parse(input))


print(f"Part 1: {part2(INPUT, error=0):,}") # 34,393
print(f"Part 2: {part2(INPUT):,}")  # 83,551,068,361,379
