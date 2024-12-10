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

    routes_to_here = defaultdict(int)
    for point in area[0]:
        routes_to_here[point] += 1
    for height in range(1, 10):
        next_routes_to_here = defaultdict(int)
        for r, c in area[height]:
            for dr, dc in moves:
                if (r + dr, c + dc) in routes_to_here:
                    next_routes_to_here[r, c] += routes_to_here[r + dr, c + dc]
        routes_to_here = next_routes_to_here

    return sum(routes_to_here.values())


example = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

example_answer = 81


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
