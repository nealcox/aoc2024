import re
import sys


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

    firsts.sort()
    seconds.sort()
    while firsts:
        answer += abs(firsts.pop() - seconds.pop())

    return answer


example = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""

example_answer = 11


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
