message = input()

command = input()
while command != "Decode":
    command_args = command.split("|")
    action = command_args[0]

    current_message = ""

    if action == "Move":
        num_of_letters = int(command_args[1])
        current_message = message[num_of_letters:] + message[:num_of_letters]
        message = current_message
    elif action == "Insert":
        i = int(command_args[1])
        value = command_args[2]
        current_message = message[:i] + value + message[i:]
        message = current_message
    elif action == "ChangeAll":
        substring = command_args[1]
        replacement = command_args[2]

        if substring in message:
            current_message = message.replace(substring, replacement)
            message = current_message

    command = input()

print(f"The decrypted message is: {message}")
