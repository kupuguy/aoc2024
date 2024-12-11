from pathlib import Path
from collections import Counter, defaultdict

TEST = """125 17"""


def blink(n: str) -> list[str]:
    if n == "0":
        return ["1"]
    length = len(n)
    if length % 2 == 0:
        return [n[: length // 2], str(int(n[length // 2 :]))]
    return [f"{int(n)*2024}"]


def part1(input: str, blinks: int = 25) -> int:
    stones = Counter(input.split())
    for gen in range(blinks):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            for blinked in blink(stone):
                new_stones[blinked] += count
        stones = new_stones
    return sum(stones.values())


assert part1(TEST, 6) == 22
assert part1(TEST) == 55312

INPUT = Path("input/day11.txt").read_text()
part1_total = part1(INPUT)
print(f"{part1_total=:,}")  # 198089

part2_total = part1(INPUT, 75)
print(f"{part2_total=:,}")  # 236,302,670,835,517
