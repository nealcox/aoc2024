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
    r = re.compile(r"mul\((\d+),(\d+)\)")
    for ops in r.findall(input_text):
        answer += int(ops[0]) * int(ops[1])

    return answer


example = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

example_answer = 161


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
