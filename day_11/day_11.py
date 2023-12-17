old_universe = []
with open("input.txt") as input_file:
    occupied_vertical_indexes = set()
    all_indexes = set()
    for horizontal_index, line in enumerate(input_file.readlines()):
        all_indexes.add(horizontal_index)
        new_vertical = []
        for vertical_index, symbol in enumerate(line.strip()):
            new_vertical.append(symbol)

            if symbol == "#":
                occupied_vertical_indexes.add(vertical_index)

        old_universe.append(new_vertical)

vertical_indexes_to_expand = all_indexes - occupied_vertical_indexes

new_universe = []

for i in old_universe:
    new_universe.append(i)

    if "#" not in i:
        new_universe.append(i)

for vertical_index in vertical_indexes_to_expand:
    for i in new_universe:
        i.insert(vertical_index + 1, ".")


galaxies_coordinates = []
for index_i, i in enumerate(new_universe):
    for index_j, j in enumerate(i):
        if j == "#":
            galaxies_coordinates.append((index_i, index_j))

part_1 = 0
for i, start_galaxy in enumerate(galaxies_coordinates):
    for j in range(i + 1, len(galaxies_coordinates)):
        destination_galaxy = galaxies_coordinates[j]
        part_1 += abs(start_galaxy[0] - destination_galaxy[0]) + abs(start_galaxy[1] - destination_galaxy[1])

print(f"Part 1. Answer: {part_1}")
