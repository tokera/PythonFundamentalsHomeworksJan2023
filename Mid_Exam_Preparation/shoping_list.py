initial_list = input().split("!")

command = input()
while command != "Go Shopping!":
    command_args = command.split()
    key_word = command_args[0]
    item = command_args[1]

    if item not in initial_list:
        if key_word == "Urgent":
            initial_list.insert(0, item)
    else:
        if key_word == "Unnecessary":
            initial_list.remove(item)
        elif key_word == "Correct":
            new_item = command_args[2]
            index = initial_list.index(item)
            initial_list[index] = new_item
        elif key_word == "Rearrange":
            initial_list.append(initial_list.pop(initial_list.index(item)))

    command = input()

print(", ".join(initial_list))
