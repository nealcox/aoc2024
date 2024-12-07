import sys


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    move = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    turn = {"^": ">", ">": "v", "v": "<", "<": "^"}

    blocks = set()
    seen = set()

    lines = input_text.splitlines()
    height = len(lines)
    width = len(lines[0])

    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            if char == ".":
                pass
            elif char == "#":
                blocks.add((r, c))
            elif char in "^>v<":
                pos = (r, c)
                seen.add(pos)
                direction = char

    while True:
        next_pos = (pos[0] + move[direction][0], pos[1] + move[direction][1])
        if next_pos in blocks:
            direction = turn[direction]
        elif not (0 <= next_pos[0] < width) or not (0 <= next_pos[1] < height):
            break
        else:
            pos = next_pos
            seen.add(pos)

    return len(seen)


example = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

example_answer = 41


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
