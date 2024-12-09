from pathlib import Path
from typing import Sequence
from collections import deque
from dataclasses import dataclass

TEST = """2333133121414131402"""


def parse(input: str) -> Sequence[tuple[int, int]]:
    file_id = 0
    blocks = deque(int(n) for n in input)
    if len(input) % 2 == 0:
        blocks.pop()
    tail_id = len(blocks) // 2
    tail_length = blocks.pop()
    blocks.pop()
    while blocks:
        yield file_id, blocks.popleft()
        file_id += 1
        if blocks:
            space = blocks.popleft()
            while space > 0:
                gap = min(space, tail_length)
                yield tail_id, gap
                tail_length -= gap
                space -= gap
                if tail_length == 0:
                    if blocks:
                        tail_id -= 1
                        tail_length = blocks.pop()
                    else:
                        tail_id = 0
                        tail_length = 9
                    if blocks:
                        blocks.pop()
    yield tail_id, tail_length


def part1(input: str) -> int:
    block = 0
    checksum = 0
    for file_id, length in parse(input):
        checksum += (length * (block + block + length - 1)) // 2 * file_id
        block += length
    return checksum


assert part1(TEST) == 1928

INPUT = Path("input/day9.txt").read_text()
part1_total = part1(INPUT)
print(f"{part1_total=:,}")  # 6241633730082


@dataclass
class Blockrun:
    file_id: int
    start: int
    length: int


def parse2(input: str) -> tuple[list[Blockrun], list[Blockrun]]:
    occupied: list[Blockrun] = []
    free: list[Blockrun] = []
    start = 0
    if len(input) % 2 != 0:
        input += "0"
    for file_id, (a, b) in enumerate(zip(input[::2], input[1::2])):
        length = int(a)
        occupied.append(Blockrun(file_id=file_id, start=start, length=length))
        start += length
        length = int(b)
        free.append(Blockrun(file_id=-1, start=start, length=length))
        start += length
    return occupied, free


def check(blocks: list[Blockrun]) -> int:
    checksum = sum(
        (block.length * (block.start * 2 + block.length - 1)) // 2 * block.file_id
        for block in blocks
    )
    return checksum


def part2(input: str) -> int:
    occupied, free = parse2(input)
    for b in occupied[::-1]:
        for f in free:
            if f.start >= b.start:
                break
            if f.length >= b.length:
                b.start = f.start
                f.start += b.length
                f.length -= b.length
                break
    return check(occupied)


assert part2(TEST) == 2858
part2_total = part2(INPUT)
print(f"{part2_total=:,}")  # 6,265,268,809,555
