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
    for machine in input_text.split("\n\n"):
        x1, y1, x2, y2, xtarget, ytarget = (
            int(i) for i in re.findall(r"(-?\d+)", machine)
        )
        # A * x1 + B * x2 = xtarget
        # A * y1 + B * y2 = ytarget
        #
        # A * (x1*y2) + B * (x2*y2) = xtarget*y2
        # A * (y1*x2) + B * (y2*x2) = ytarget*x2
        #
        # A = ((xtarget * y2) - (ytarget*x2)) / ( x1*y2 - y1*x2)
        # B = (xtarget - A * x1) / x2
        A, remA = divmod(((xtarget * y2) - (ytarget * x2)), (x1 * y2 - y1 * x2))
        B, remB = divmod((xtarget - A * x1), x2)

        if remA == 0 and remB == 0 and A <= 100 and B <= 100:
            answer += 3 * A + B

    return answer


example = """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

example_answer = 480


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
