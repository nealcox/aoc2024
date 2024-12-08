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
    ants = defaultdict(list)
    antinodes = set()

    lines = input_text.splitlines()
    height = len(lines)
    width = len(lines[0])

    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            if char != ".":
                ants[char].append((r, c))

    for char, positions in ants.items():
        for (r1, c1), (r2, c2) in permutations(positions, 2):
            (dr, dc) = (r2 - r1, c2 - c1)
            pos = (r2, c2)
            while 0 <= pos[0] < height and 0 <= pos[1] < width:
                antinodes.add(pos)
                pos = (pos[0] + dr, pos[1] + dc)

    return len(antinodes)


example = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

example_answer = 34


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
