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
    assert len(input_text) % 2 == 1
    current_file_id = 0
    block = 0
    pos = 0
    files = []
    spaces = []

    while pos < len(input_text) - 1:
        # File
        file_length = int(input_text[pos])
        files.append((block, file_length))
        block += file_length
        pos += 1

        # Space
        space_length = int(input_text[pos])
        spaces.append((block, space_length))
        block += space_length
        pos += 1

    # Final file
    file_length = int(input_text[pos])
    files.append((block, file_length))
    block += file_length

    for file_id in range(len(files) - 1, 0, -1):
        new_block = 0
        block, file_length = files[file_id]
        for space_num, (space_block, space_length) in enumerate(spaces):
            if space_block >= block:
                break
            if space_length >= file_length:
                new_space_block = space_block + file_length
                new_space_length = space_length - file_length
                new_block = space_block
                break
        if new_block:
            files[file_id] = (new_block, file_length)
            if new_space_length:
                spaces[space_num] = (new_space_block, new_space_length)
            else:
                del spaces[space_num]

    for file_id, (block, file_length) in enumerate(files):
        for i in range(file_length):
            answer += (block + i) * file_id

    return answer


example = """\
2333133121414131402"""

example_answer = 2858


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
