from collections import deque

water_in_dispenser = int(input())

people_wants_to_get_water = deque([])

while True:
    name = input()
    if name == "Start":
        break

    people_wants_to_get_water.append(name)

command = input()
while command != "End":
    command_args = command.split()

    if command_args[0] == "refill":
        litters = int(command_args[1])
        water_in_dispenser += litters
    else:
        litters = int(command_args[0])

        if litters <= water_in_dispenser:
            water_in_dispenser -= litters
            print(f"{people_wants_to_get_water.popleft()} got water")
        else:
            print(f"{people_wants_to_get_water.popleft()} must wait")
    command = input()

print(f"{water_in_dispenser} liters left")
