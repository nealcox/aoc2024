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
    moves = {(1, 0), (0, 1), (-1, 0), (0, -1)}

    area = defaultdict(set)
    for r, row in enumerate(input_text.splitlines()):
        for c, char in enumerate(row):
            area[int(char)].add((r, c))

    can_reach = defaultdict(set)
    for point in area[9]:
        can_reach[point].add(point)
    for height in range(8, -1, -1):
        next_can_reach = defaultdict(set)
        for r, c in area[height]:
            for dr, dc in moves:
                if (r + dr, c + dc) in can_reach:
                    next_can_reach[r, c].update(can_reach[r + dr, c + dc])
        can_reach = next_can_reach

    return sum(len(s) for s in can_reach.values())


example = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

example_answer = 36


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
