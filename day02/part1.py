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
    for line in input_text.splitlines():
        numbers  = [int(i) for i in re.findall(r"(-?\d+)", line)]
        given.append(numbers)

    for report in given:
        in_order = (report == sorted(report) or report==sorted(report,reverse=True))
        diffs_ok = True
        for i, l in enumerate(report[:-1]):
            if not( 0 < abs(report[i+1] - l) < 4):
                diffs_ok = False
                break
        if in_order and diffs_ok:
            answer += 1
            print(f"OK {report}")
        else:
            print(f"XX {report}")
    return answer


example = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

example_answer = 2


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
