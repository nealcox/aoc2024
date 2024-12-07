import re
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
    given = []
    m = 0
    for line in input_text.splitlines():
        target_text, rest_text = line.split(": ")
        target, rest = (int(target_text),  tuple(int(i) for i in rest_text.split()))
        m = max(m, len(rest))
        sums = set()
        sums.add( rest[0])
        for i in rest[1:]:
            next_sums = set()
            for prev in sums:
                next_sums.add(prev + i)
                next_sums.add(prev * i)
            sums = next_sums
        if target in sums:
            answer += target
        print(sums, rest)

    return answer


def parse(s):
    given = None
    # given = partlines(s)
    # given = get_one_int_per_line(s)
    # given = get_re(s)
    # given = get_all_ints(s)
    given = get_map(s)  # given is tuple (area_map, height, width)
    return given


def partlines(s):
    given = []
    for line in s.split("\n"):
        line = line.strip()
        given.append(line)
    return given


def get_map(s):
    area = defaultdict(lambda: float("inf"))

    lines = s.splitlines()
    height = len(lines)
    width = len(lines[0])

    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            area[r, c] = int(char)
    given = (area, height, width)
    return given


def get_one_int_per_line(s):
    ints = []
    for line in s.split("\n"):
        ints.append(int(line))
    return ints


def get_re(s):
    given = []
    r = re.compile(r"(\w+) (\d+)")
    for m in r.findall(s):
        given.append((m[0], int(m[1])))
    return given


def get_all_ints(s):
    return (int(i) for i in re.findall(r"(-?\d+)", s))


example = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

example_answer = 3749


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
