def is_valid_index(i, collection):
    return 0 <= i < len(collection)


string_of_stops = input()

command = input()
while command != "Travel":
    command_args = command.split(":")
    action = command_args[0]

    current_string = ""

    if action == "Add Stop":
        index = int(command_args[1])
        string = command_args[2]
        if is_valid_index(index, string_of_stops):
            current_string = string_of_stops[:index] + string + string_of_stops[index:]
            string_of_stops = current_string
    elif action == "Remove Stop":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        if is_valid_index(start_idx, string_of_stops) and is_valid_index(end_idx, string_of_stops):
            current_string = string_of_stops[:start_idx] + string_of_stops[end_idx + 1:]
            string_of_stops = current_string
    elif action == "Switch":
        old_string = command_args[1]
        new_string = command_args[2]

        if old_string in string_of_stops:
            current_string = string_of_stops.replace(old_string, new_string)
            string_of_stops = current_string

    print(string_of_stops)

    command = input()

print(f"Ready for world tour! Planned stops: {string_of_stops}")
