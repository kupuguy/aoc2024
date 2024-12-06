from pathlib import Path
from functools import cmp_to_key

TEST = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def parse(input: str) -> tuple[dict[int, set[int]], list[list[int]]]:
    rulemap: dict[int, set[int]] = {}
    recs: list[list[int]] = []
    rules, _, records = input.partition("\n\n")
    for r in rules.splitlines():
        a, _, b = r.partition("|")
        if int(a) in rulemap:
            rulemap[int(a)].add(int(b))
        else:
            rulemap[int(a)] = {int(b)}

    for r in records.splitlines():
        recs.append([int(n) for n in r.split(",")])

    return rulemap, recs


def is_valid(record: list[int], rulemap: dict[int, set[int]]) -> bool:
    seen = set()
    for r in record:
        if r in rulemap and (rulemap[r] & seen):
            return False

        seen.add(r)
    return True


def part1(input: str) -> int:
    rulemap, records = parse(input)
    valid = [r for r in records if is_valid(r, rulemap)]

    middles = [r[len(r) // 2] for r in valid]
    return sum(middles)


assert part1(TEST) == 143
INPUT = Path("input/day5.txt").read_text()
print(f"{part1(INPUT)=}")  # 5087


def part2(input: str) -> int:
    def cmp_fn(a: int, b: int) -> int:
        if a in rulemap and rulemap[a] & {b}:
            return -1
        elif b in rulemap and rulemap[b] & {a}:
            return 1
        return b - a

    rulemap, records = parse(input)

    invalid = [
        sorted(r, key=cmp_to_key(cmp_fn)) for r in records if not is_valid(r, rulemap)
    ]

    middles = [r[len(r) // 2] for r in invalid]
    return sum(middles)


assert part2(TEST) == 123
print(f"{part2(INPUT)=}")  # 4971
