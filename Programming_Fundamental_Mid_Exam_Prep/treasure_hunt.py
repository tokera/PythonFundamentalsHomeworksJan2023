treasure_chest = input().split("|")

command = input()
while command != "Yohoho!":
    command_args = command.split()
    action = command_args[0]

    if action == "Loot":
        for i in range(1, len(command_args)):
            if command_args[i] not in treasure_chest:
                treasure_chest.insert(0, command_args[i])
    elif action == "Drop":
        idx = int(command_args[1])
        if 0 <= idx < len(treasure_chest):
            treasure_chest.append(treasure_chest.pop(idx))
    elif action == "Steal":
        count = int(command_args[1])
        if count > len(treasure_chest):
            count = len(treasure_chest)
        stolen_items = []
        for _ in range(count):
            stolen_items.insert(0, treasure_chest.pop(-1))
        print(", ".join(stolen_items))

    command = input()

if treasure_chest:
    treasure_lengths = [len(x) for x in treasure_chest]
    average_treasure_gain = sum(treasure_lengths) / len(treasure_lengths)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
