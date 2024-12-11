import sys
from collections import defaultdict


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    answer = 0

    # File at end, used to fill in the spaces
    fill_file_id = (len(input_text) - 1) // 2
    fill_from_pos = len(input_text) - 1
    fill_blocks_available = int(input_text[fill_from_pos])

    current_file_id = 0
    block = 0
    pos = 0
    while current_file_id < fill_file_id:
        # Files from start in place
        current_file_blocks = int(input_text[pos])
        for _ in range(current_file_blocks):
            answer += block * current_file_id
            block += 1
        current_file_id += 1
        pos += 1

        # Fill empty blocks
        blocks_to_fill = int(input_text[pos])

        while blocks_to_fill and current_file_id < fill_file_id:
            for _ in range(min(blocks_to_fill, fill_blocks_available)):
                answer += block * fill_file_id
                block += 1
                blocks_to_fill -= 1
                fill_blocks_available -= 1

            if fill_blocks_available == 0:
                fill_file_id -= 1
                fill_from_pos -= 2
                fill_blocks_available = int(input_text[fill_from_pos])
        pos += 1

    # Fill from last file
    if current_file_id == fill_file_id:
        for _ in range(fill_blocks_available):
            answer += block * current_file_id
            block += 1

    return answer


example = """\
2333133121414131402"""

example_answer = 1928


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
