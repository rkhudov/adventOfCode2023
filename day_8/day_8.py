with open("input.txt") as input_file:
    lines = input_file.readlines()

    instructions = lines[0].strip()
    data = {}

    for line in lines[2:]:
        line = line.strip()
        root, next_items = line.split(" = ")
        left, right = next_items[1:-1].split(", ")

        data[root] = {
            "L": left,
            "R": right,
        }

start = "AAA"
end = "ZZZ"
pointer = data[start]
flag = True
count = 0

while flag:
    for instruction in instructions:
        count += 1

        if pointer[instruction] != end:
            pointer = data[pointer[instruction]]
        else:
            flag = False

print(f"Part 1: {count}")

