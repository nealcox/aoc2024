import re
import sys
from collections import Counter


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    answer = 0
    firsts = []
    seconds = []
    r = re.compile(r"(\d+) +(\d+)")
    for m in r.findall(input_text):
        firsts.append(int(m[0]))
        seconds.append(int(m[1]))

    c = Counter(seconds)
    for f in firsts:
        answer += f * c[f]

    return answer


example = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""

example_answer = 31


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
