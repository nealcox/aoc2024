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
                next_sums.add(prev * (10 ** len(f"{i}")) + i)
            sums = next_sums
        if target in sums:
            answer += target

    return answer


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

example_answer = 11387


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
