from collections import defaultdict, Counter


def find_common_elements(list_1: list[int], list_2: list[int]) -> list[int]:
    list_1 = Counter(list_1)
    list_2 = Counter(list_2)
    return list((list_1 & list_2).elements())


def count_score(numbers: list[int]) -> int:
    score = 0
    for index, number in enumerate(numbers):
        if index == 0:
            score += 1
        else:
            score *= 2
    return score


part_1_result = 0
part_2_result = 0
with open("input.txt") as input_file:
    data = defaultdict(int)

    for card_number, line in enumerate(input_file.readlines()):
        card_number += 1
        line = line[:-1]

        numbers = line.split(":")[1].split("|")
        winning_numbers = [int(number) for number in numbers[0].split()]
        my_numbers = [int(number) for number in numbers[1].split()]

        common_elements = find_common_elements(list_1=winning_numbers, list_2=my_numbers)
        score = count_score(numbers=common_elements)
        part_1_result += score

        if common_elements:
            data[card_number] += 1

            for i in range(card_number + 1, len(common_elements) + card_number + 1):
                data[i] += data[card_number]
        else:
            data[card_number] += 1


print(f"Part 1. Answer: {part_1_result}")
print(f"Part 2. Answer: {sum(data.values())}")
