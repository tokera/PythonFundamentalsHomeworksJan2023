message = input()

while True:
    command = input()
    if command == "Decode":
        break

    command_args = command.split("|")
    action = command_args[0]

    if action == "Move":
        num_of_letters = int(command_args[1])
        message = message[num_of_letters:] + message[:num_of_letters]
    elif action == "Insert":
        index = int(command_args[1])
        value = command_args[2]
        message = message[:index] + value + message[index:]
    elif action == "ChangeAll":
        substring = command_args[1]
        replacement = command_args[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")
