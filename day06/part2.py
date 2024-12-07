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

    move = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    turn = {"^": ">", ">": "v", "v": "<", "<": "^"}

    blocks = set()
    seen = defaultdict(int)
    track = []
    answer = 0

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
                direction = char
                seen[pos] += 1

    while True:
        next_pos = (pos[0] + move[direction][0], pos[1] + move[direction][1])
        if next_pos in blocks:
            direction = turn[direction]
        elif not (0 <= next_pos[0] < width) or not (0 <= next_pos[1] < height):
            break
        else:
            pos = next_pos
            track.append((direction, pos))
            seen[pos] += 1

    while len(track) > 1:
        _, block_pos = track.pop()
        seen[block_pos] -= 1
        test_blocks = blocks.copy()
        test_blocks.add(block_pos)
        if seen[block_pos] == 0 and ends_in_loop(
            track[:], test_blocks, width, height, move, turn
        ):
            answer += 1

    return answer


def ends_in_loop(track, blocks, width, height, move, turn):
    direction, pos = track.pop()

    while True:
        next_pos = (pos[0] + move[direction][0], pos[1] + move[direction][1])
        if next_pos in blocks:
            direction = turn[direction]
        elif not (0 <= next_pos[0] < width) or not (0 <= next_pos[1] < height):
            return False
        elif (direction, next_pos) in track:
            return True
        else:
            pos = next_pos
            track.append((direction, pos))


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

example_answer = 6


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
