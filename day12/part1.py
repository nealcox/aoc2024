import sys
from collections import defaultdict
from itertools import permutations


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    answer = 0

    area = defaultdict(set)
    for r, row in enumerate(input_text.splitlines()):
        for c, char in enumerate(row):
            area[char].add((r, c))

    regions = set()
    for flower in area:
        while area[flower]:
            region = set()
            to_check = set()
            p = area[flower].pop()
            region.add(p)
            to_check.add(p)
            while to_check:
                next_to_check = set()
                for r, c in to_check:
                    for adj in adjacent(r, c):
                        if adj in area[flower]:
                            region.add(adj)
                            next_to_check.add(adj)
                            area[flower].discard(adj)
                to_check = next_to_check
            regions.add(frozenset(region))

    for region in regions:
        internal_fences = 0
        for p1, p2 in permutations(region, 2):
            if p1 in adjacent(*p2):
                internal_fences += 1

        fences = 4 * len(region) - internal_fences
        answer += len(region) * fences

    return answer


def adjacent(r, c):
    return {(r + dr, c + dc) for (dr, dc) in {(1, 0), (-1, 0), (0, 1), (0, -1)}}


example = """\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

example_answer = 1930


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
