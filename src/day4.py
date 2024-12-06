from pathlib import Path

TEST = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def part1(input: str) -> int:
    count = 0
    line_length = len(input.splitlines()[0]) + 1
    for n in range(len(input)):
        # if input[n] != 'X':
        #     continue
        words = [
            input[n : n + 4 : 1],
            input[n :: line_length - 1][:4],
            input[n::line_length][:4],
            input[n :: line_length + 1][:4],
        ]
        count += sum(1 if w in ("XMAS", "SAMX") else 0 for w in words)
    return count


assert part1(TEST) == 18
INPUT = Path("input/day4.txt").read_text()
print(f"{part1(INPUT)=}")  # 2654


def part2(input: str) -> int:
    count = 0
    line_length = len(input.splitlines()[0]) + 1
    for n in range(len(input)):
        d1 = input[n : n + 2 * line_length + 3 : line_length + 1]
        d2 = input[n + 2 : n + 2 * line_length + 1 : line_length - 1]
        if d1 in ("MAS", "SAM") and d2 in ("MAS", "SAM"):
            count += 1
    return count


assert part2(TEST) == 9
print(f"{part2(INPUT)=}")  # 1990
