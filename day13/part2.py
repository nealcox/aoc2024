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
        xtarget += 10000000000000
        ytarget += 10000000000000
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

        if remA == 0 and remB == 0:
            answer += 3 * A + B

    return answer


if __name__ == "__main__":
    exit(main())
