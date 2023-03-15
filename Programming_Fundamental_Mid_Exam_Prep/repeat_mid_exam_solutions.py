neighborhood = [int(x) for x in input().split("@")]

current_index = 0

command = input()
while command != "Love!":
    command_args = command.split()
    length = int(command_args[1])

    current_index += length
    if current_index >= len(neighborhood):
        current_index = 0

    if neighborhood[current_index] != 0:
        neighborhood[current_index] -= 2
        if neighborhood[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")
    else:
        print(f"Place {current_index} already had Valentine's day.")

    command = input()

houses_not_celebrate = [x for x in neighborhood if x != 0]

if houses_not_celebrate:
    print(f"Cupid's last position was {current_index}.")
    print(f"Cupid has failed {len(neighborhood) - neighborhood.count(0)} places.")
else:
    print("Mission was successful.")
