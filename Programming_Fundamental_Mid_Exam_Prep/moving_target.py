def is_valid_index(idx, collection):
    if 0 <= idx < len(collection):
        return True
    return False


targets = [int(x) for x in input().split()]

command = input()
while command != "End":
    command_args = command.split()
    cmd = command_args[0]
    index = int(command_args[1])

    if cmd == "Shoot":
        power = int(command_args[2])
        if is_valid_index(index, targets):
            targets[index] -= power

            if targets[index] <= 0:
                targets.pop(index)
    elif cmd == "Add":
        value = int(command_args[2])
        if is_valid_index(index, targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif cmd == "Strike":
        radius = int(command_args[2])
        start_idx = index - radius
        end_idx = index + radius

        if is_valid_index(start_idx, targets) and is_valid_index(end_idx, targets):
            for i in range(end_idx, start_idx - 1, - 1):
                targets.pop(i)
        else:
            print("Strike missed!")

    command = input()

print("|".join([str(x) for x in targets]))
