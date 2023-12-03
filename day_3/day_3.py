import string
import re
import math


def is_symbol(char: str) -> bool:
    if char == ".":
        return False
    return char in string.punctuation


with open("input.txt") as input_file:
    lines = input_file.readlines()
    number_data = {}
    symbol_data = {}

    for vertical_index, line in enumerate(lines):
        line = line[:-1]

        for i in re.finditer(r'\d+', line):
            number_data[(vertical_index, tuple(range(i.start(), i.end())))] = int(i.group())

        for horizontal_index, char in enumerate(line):
            if char in string.punctuation and char != ".":
                symbol_data[(vertical_index, horizontal_index)] = char


part_1_result = 0
part_2_result = 0
for symbol_position, symbol in symbol_data.items():
    count = 0
    numbers = []

    for number_position, number in number_data.items():
        if (symbol_position[0] - 1) in number_position or symbol_position[0] in number_position or (symbol_position[0] + 1) in number_position:
            if (symbol_position[1] - 1) in number_position[1] or symbol_position[1] in number_position[1] or (symbol_position[1] + 1) in number_position[1]:
                part_1_result += number

                if symbol == "*":
                    numbers.append(number)
                    count += 1

                if count > 1:
                    part_2_result += math.prod(numbers)

print(f"Part 1: {part_1_result}")
print(f"Part 2: {part_2_result}")
