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
    area = defaultdict(lambda: " ")

    lines = input_text.splitlines()
    height = len(lines)
    width = len(lines[0])

    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            area[r, c] = char

    for r in range(height):
        for c in range(width):
            if (
                area[r, c] == "X"
                and area[r + 1, c] == "M"
                and area[r + 2, c] == "A"
                and area[r + 3, c] == "S"
            ):
                answer += 1
            if (
                area[r, c] == "X"
                and area[r - 1, c] == "M"
                and area[r - 2, c] == "A"
                and area[r - 3, c] == "S"
            ):
                answer += 1
            if (
                area[r, c] == "X"
                and area[r, c + 1] == "M"
                and area[r, c + 2] == "A"
                and area[r, c + 3] == "S"
            ):
                answer += 1
            if (
                area[r, c] == "X"
                and area[r, c - 1] == "M"
                and area[r, c - 2] == "A"
                and area[r, c - 3] == "S"
            ):
                answer += 1

            if (
                area[r, c] == "X"
                and area[r + 1, c + 1] == "M"
                and area[r + 2, c + 2] == "A"
                and area[r + 3, c + 3] == "S"
            ):
                answer += 1
            if (
                area[r, c] == "X"
                and area[r - 1, c - 1] == "M"
                and area[r - 2, c - 2] == "A"
                and area[r - 3, c - 3] == "S"
            ):
                answer += 1
            if (
                area[r, c] == "X"
                and area[r - 1, c + 1] == "M"
                and area[r - 2, c + 2] == "A"
                and area[r - 3, c + 3] == "S"
            ):
                answer += 1
            if (
                area[r, c] == "X"
                and area[r + 1, c - 1] == "M"
                and area[r + 2, c - 2] == "A"
                and area[r + 3, c - 3] == "S"
            ):
                answer += 1

    return answer


example = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

example_answer = 18


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
