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
        if is_safe(report):
            answer += 1
            print(f"OK {report}")
        else:
            print(f"XX {report}")
            sub_is_safe = False
            for i in range(len(report)):
                if is_safe(report[:i] + report[i+1:]):
                    sub_is_safe = True
                    print(f"YY {report[:i] + report[i+1:]}")
            if sub_is_safe:
                answer += 1
    return answer


def is_safe(report):
    in_order = (report == sorted(report) or report==sorted(report,reverse=True))
    diffs_ok = True
    for i, l in enumerate(report[:-1]):
        if not( 0 < abs(report[i+1] - l) < 4):
            diffs_ok = False
            break
    return in_order and diffs_ok

example = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

example_answer = 4


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
