import sys
from collections import defaultdict


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
    seen = set()
    for flower in area:
        while area[flower]:
            region = set()
            p = area[flower].pop()
            region.add(p)
            to_check = set()
            to_check.add(p)
            seen.add(p)
            while to_check:
                next_to_check = set()
                for r, c in to_check:
                    for adj in adjacent(r, c):
                        if adj in area[flower] and adj not in seen:
                            region.add(adj)
                            next_to_check.add(adj)
                            area[flower].discard(adj)
                to_check = next_to_check
            regions.add(frozenset(region))

    for region in regions:
        answer += len(region) * num_sides(region)

    return answer


def num_sides(region):

    moves = {(1, 0): (0, 1), (-1, 0): (0, 1), (0, 1): (1, 0), (0, -1): (1, 0)}

    external = defaultdict(list)
    for dr, dc in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
        for r, c in region:
            if (r + dr, c + dc) not in region:
                external[(dr, dc)].append((r, c))

    for d, v in external.items():
        if d in {(1, 0), (0, 1)}:
            v.sort()
        else:
            v.sort(key=lambda x: (x[1], x[0]))

    num_sides = 0
    for d, l in external.items():
        num_sides += 1
        dr, dc = moves[d]
        for i, (r, c) in enumerate(l[:-1]):
            if (r + dr, c + dc) not in l:
                num_sides += 1

    return num_sides


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

example_answer = 1206


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
