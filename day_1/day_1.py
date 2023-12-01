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


def find_all_occurrences(main_string, substring):
    occurrences = [i for i in range(len(main_string)) if main_string.startswith(substring, i)]
    return occurrences


def get_number(line:str) -> int:
    digits = {}
    for word, digit in WORD_TO_DIGITS_MAPPING.items():
        for word_occurrence_index in find_all_occurrences(line, word):
            digits[word_occurrence_index] = digit

        for digit_occurrence_index in find_all_occurrences(line, digit):
            digits[digit_occurrence_index] = digit

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
