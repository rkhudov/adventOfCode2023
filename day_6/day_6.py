with open("input.txt") as input_file:
    times = []
    time = 0
    distances = []
    distance = 0
    for index, line in enumerate(input_file.readlines()):
        line = line.strip()

        if index == 0:
            times = [int(number) for number in line.split(":")[1].split()]
            time = int("".join([number for number in line.split(":")[1].split()]))
        elif index == 1:
            distances = [int(number) for number in line.split(":")[1].split()]
            distance = int("".join([number for number in line.split(":")[1].split()]))
        continue

print(time)
print(distance)
count = 0
for t in range(time + 1):
    if t * (time - t) > distance:
        count += 1

print(f"Part 2: {count}")

time_distance_map = dict(zip(times, distances))
result = 1
for time, distance in time_distance_map.items():
    count = 0

    for t in range(time + 1):
        if t * (time - t) > distance:
            count += 1

    result *= count

print(f"Part 1: {result}")
