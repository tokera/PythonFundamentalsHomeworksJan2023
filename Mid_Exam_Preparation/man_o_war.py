def is_valid_index(idx, collection):
    if 0 <= idx < len(collection):
        return True
    return False


pirate_ship_status = [int(x) for x in input().split(">")]
warship_status = [int(x) for x in input().split(">")]
max_health_capacity = int(input())

command = input()
while command != "Retire":
    command_args = command.split()
    key_word = command_args[0]

    if key_word == "Fire":
        index = int(command_args[1])
        damage = int(command_args[2])

        if is_valid_index(index, warship_status):
            warship_status[index] -= damage

            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit(0)
    elif key_word == "Defend":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        damage = int(command_args[3])

        if is_valid_index(start_idx, pirate_ship_status) \
                and is_valid_index(end_idx, pirate_ship_status) \
                and start_idx <= end_idx:
            for i in range(start_idx, end_idx + 1):
                pirate_ship_status[i] -= damage

                if pirate_ship_status[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit(0)
    elif key_word == "Repair":
        index = int(command_args[1])
        health = int(command_args[2])
        if is_valid_index(index, pirate_ship_status):
            pirate_ship_status[index] += health

            if pirate_ship_status[index] > max_health_capacity:
                pirate_ship_status[index] = max_health_capacity

    elif key_word == "Status":
        sections_needed_to_repair = [x for x in pirate_ship_status if x < max_health_capacity * (20 / 100)]
        print(f"{len(sections_needed_to_repair)} sections need repair.")

    command = input()

print(f"Pirate ship status: {sum(pirate_ship_status)}")
print(f"Warship status: {sum(warship_status)}")
