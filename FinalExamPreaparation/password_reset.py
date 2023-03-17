text = input()

command = input()
while command != "Done":
    command_args = command.split()
    action = command_args[0]

    current_text = ""

    if action == "TakeOdd":
        for i in range(1, len(text), 2):
            current_text += text[i]
        text = current_text
        print(text)
    elif action == "Cut":
        index = int(command_args[1])
        length = int(command_args[2])
        substring = text[index:index + length]
        current_text = text.replace(substring, "", 1)
        text = current_text
        print(text)
    elif action == "Substitute":
        substring = command_args[1]
        substitute = command_args[2]

        if substring in text:
            current_text = text.replace(substring, substitute)
            text = current_text
            print(text)
        else:
            print("Nothing to replace!")

    command = input()
print(f"Your password is: {text}")
