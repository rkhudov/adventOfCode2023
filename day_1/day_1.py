WORD_TO_DIGITS_MAPPING = {
    "nine": "9",
    "eight": "8",
    "seven": "7",
    "six": "6",
    "five": "5",
    "four": "4",
    "three": "3",
    "two": "2",
    "one": "1",
}


def get_number(line:str) -> int:
    digits = {}
    for word, digit in WORD_TO_DIGITS_MAPPING.items():
        for i in range(len(line)):
            if line.startswith(word, i):
                digits[i] = digit
            if line.startswith(digit, i):
                digits[i] = digit

    second_digit_index = max(digits.keys())
    try:
        first_digit_index = min([key for key in digits.keys() if key >= 0])
    except ValueError:
        first_digit_index = second_digit_index
    return int(f"{digits[first_digit_index]}{digits[second_digit_index]}")


result = 0
with open("input.txt") as input_file:
    lines = input_file.readlines()

    for line in lines:
        line = line[:-1]
        result += get_number(line=line)

print(result)
