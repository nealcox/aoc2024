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
    locks = []
    keys = []
    for lock_or_key in input_text.split("\n\n"):
        if lock_or_key.startswith("#"):
            locks.append(get_nums(lock_or_key, "."))
        else:
            keys.append(get_nums(lock_or_key, "#"))
    for lock in locks:
        for key in keys:
            pins = zip(lock, key)
            if all(sum(p) < 6 for p in pins):
                answer += 1

    return answer


def get_nums(item, char):
    print(item, "\n", char)
    lines = zip(*item.split())
    if char == ".":
        return tuple(l.index(char) - 1 for l in lines)
    else:
        return tuple(6 - l.index(char) for l in lines)


example = """\
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""

example_answer = 3


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
