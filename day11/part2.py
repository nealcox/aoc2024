import sys
from functools import cache

def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    return sum(blink(int(i),75) for i in input_text.split())


@cache
def blink(i, times):
    if times == 0:
        return 1
    elif i == 0:
        return blink(1,times - 1)
    else:
        i_s= f"{i}"
        l = len(i_s)
        if l%2:
            return blink(i*2024, times -1)
        else:
            return blink(int(i_s[:l//2]), times -1) + blink(int(i_s[l//2:]), times - 1)


if __name__ == "__main__":
    exit(main())
