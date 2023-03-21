raw_key = input()

while True:
    command = input()
    if command == "Generate":
        break

    command_args = command.split(">>>")
    action = command_args[0]

    if action == "Contains":
        substring = command_args[1]

        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
            continue

        print("Substring not found!")
    elif action == "Flip":
        key = command_args[1]
        start = int(command_args[2])
        stop = int(command_args[3])
        substring = raw_key[start:stop]

        if key == "Upper":
            substring = substring.upper()
        else:
            substring = substring.lower()

        raw_key = raw_key[:start] + substring + raw_key[stop:]
        print(raw_key)
    elif action == "Slice":
        start_idx = int(command_args[1])
        stop_idx = int(command_args[2])

        raw_key = raw_key[:start_idx] + raw_key[stop_idx:]
        print(raw_key)

print(f"Your activation key is: {raw_key}")
