import re
import sys
from functools import cmp_to_key


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    def compare(a, b):
        if a == b:
            return 0
        elif (a, b) in rules:
            return -1
        else:
            return 1

    answer = 0
    rules_text, pages_text = input_text.split("\n\n")
    rules = []
    to_sort = []
    for rule in rules_text.splitlines():
        m = rule.split("|")
        rules.append((m[0], m[1]))

    updates = [update.split(",") for update in pages_text.splitlines()]
    for update in updates:
        correct = True
        for i, num in enumerate(update[:-1]):
            if (num, update[i + 1]) not in rules:
                correct = False
                break
        if not correct:
            to_sort.append(update)
    sorted_updates = [sorted(update, key=cmp_to_key(compare)) for update in to_sort]

    for update in sorted_updates:
        answer += int(update[(len(update) - 1) // 2])

    return answer


example = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

example_answer = 123


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())