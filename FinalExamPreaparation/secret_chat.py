concealed_message = input()

command = input()
while command != "Reveal":
    command_args = command.split(":|:")
    operation = command_args[0]

    current_msg = ""

    if operation == "InsertSpace":
        idx = int(command_args[1])
        current_msg = concealed_message[:idx] + " " + concealed_message[idx:]
        concealed_message = current_msg
        print(concealed_message)
    elif operation == "Reverse":
        substring = command_args[1]
        if substring in concealed_message:
            current_msg = concealed_message.replace(substring, "", 1) + substring[::-1]
            concealed_message = current_msg
            print(concealed_message)
        else:
            print("error")

    elif operation == "ChangeAll":
        substring = command_args[1]
        replacement = command_args[2]
        current_msg = concealed_message.replace(substring, replacement)
        concealed_message = current_msg
        print(concealed_message)

    command = input()

print(f"You have a new text message: {concealed_message}")
