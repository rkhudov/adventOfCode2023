def get_number(sequence: list[int]) -> int:
    if all(number == sequence[0] for number in sequence):
        return sequence[0]

    next_sequence = [sequence[i+1] - sequence[i] for i in range(len(sequence) - 1)]
    return get_number(next_sequence) + sequence[-1]


part_1 = 0
part_2 = 0
with open("input.txt") as input_file:
    for line in input_file.readlines():
        sequence = [int(number) for number in line.strip().split()]

        next_number = get_number(sequence=sequence)
        part_1 += next_number

        next_number = get_number(sequence=sequence[::-1])
        part_2 += next_number

print(f"Part 1. Answer: {part_1}")
print(f"Part 2. Answer: {part_2}")
