from collections import defaultdict
ALL_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def check_possible_game(plays_info: str, game_id: int) -> int:
    for play_info in plays_info.split(";"):
        cubes_info = play_info.split(",")

        for cube_info in cubes_info:
            number, color = cube_info.strip().split()

            if int(number) > ALL_CUBES[color]:
                return 0
    return game_id


def get_minimum_set_of_cubes(plays_info: str) -> list[int]:
    required_number_of_cubes = defaultdict(int)
    for play_info in plays_info.split(";"):
        cubes_info = play_info.split(",")

        for cube_info in cubes_info:
            number, color = cube_info.strip().split()

            if int(number) > required_number_of_cubes[color]:
                required_number_of_cubes[color] = int(number)

    return list(required_number_of_cubes.values())


def part_1(lines: list[str]) -> int:
    result = 0
    game_id = 0
    for line in lines:
        game_id += 1
        _, plays_info = line.split(":")
        result += check_possible_game(plays_info=plays_info, game_id=game_id)

    return result


def part_2(lines: list[str]) -> int:
    result = 0
    for line in lines:
        _, plays_info = line.split(":")
        minimum_set_of_cubes = get_minimum_set_of_cubes(plays_info=plays_info)

        prod = 1
        for number_of_cubes in minimum_set_of_cubes:
            prod *= number_of_cubes
        result += prod

    return result


with open("input.txt") as input_file:
    lines = input_file.readlines()

    print(f"Part 1. Answer: {part_1(lines=lines)}")
    print(f"Part 2. Answer: {part_2(lines=lines)}")
