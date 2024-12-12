from pathlib import Path
from dataclasses import dataclass

TEST0 = """AAAA
BBCD
BBCC
EEEC"""

TEST = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


@dataclass
class Garden:
    plant: str
    locations: set[complex]

    @property
    def area(self) -> int:
        return len(self.locations)

    @property
    def perimeter(self) -> int:
        return sum(
            4 - len({p + 1, p - 1, p + 1j, p - 1j} & self.locations)
            for p in self.locations
        )

    @property
    def sides(self) -> int:
        """Sides is same as counting corners"""
        locations = self.locations
        corners = 0
        for pos in self.locations:
            top, left, bottom, right = (
                pos - 1j in locations,
                pos - 1 in locations,
                pos + 1j in locations,
                pos + 1 in locations,
            )
            tl = not (top or left) or (top and left and pos - 1 - 1j not in locations)
            tr = not (top or right) or (top and right and pos + 1 - 1j not in locations)
            bl = not (bottom or left) or (
                bottom and left and pos - 1 + 1j not in locations
            )
            br = not (bottom or right) or (
                bottom and right and pos + 1 + 1j not in locations
            )
            corners += tl + tr + bl + br
        return corners


def find_gardens(input: str) -> list[Garden]:
    fullmap: dict[complex, str] = {
        complex(x, y): g
        for y, row in enumerate(input.splitlines())
        for x, g in enumerate(row)
    }

    gardens: list[Garden] = []
    gardenmap: dict[complex, Garden] = {}

    for pos, g in fullmap.items():
        neighbour_pos = {
            p
            for p in ({pos + 1, pos - 1, pos + 1j, pos - 1j} & fullmap.keys())
            if fullmap[p] == g
        }
        neighbours = [gardenmap[n] for n in neighbour_pos if n in gardenmap]
        if not neighbours:
            garden = Garden(g, {pos})
            gardenmap[pos] = garden
            gardens.append(garden)
        else:
            garden = neighbours[0]
            garden.locations.add(pos)
            gardenmap[pos] = garden
            if len(neighbours) > 1 and neighbours[0] is not neighbours[1]:
                for n in neighbours[1:]:
                    garden.locations |= n.locations
                    for p in n.locations:
                        gardenmap[p] = garden
                    gardens.remove(n)
    return gardens


def part1(input: str) -> int:
    gardens: list[Garden] = find_gardens(input)

    return sum(garden.area * garden.perimeter for garden in gardens)


assert part1(TEST0) == 140
assert part1(TEST) == 1930

INPUT = Path("input/day12.txt").read_text()
part1_total = part1(INPUT)
print(f"{part1_total=:,}")  # 1,446,042


def part2(input: str) -> int:
    gardens: list[Garden] = find_gardens(input)

    return sum(garden.area * garden.sides for garden in gardens)


assert part2(TEST0) == 80
assert part2(TEST) == 1206

part2_total = part2(INPUT)
print(f"{part2_total=:,}")  # 902,742
