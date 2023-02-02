command = input()

count_of_coffee = 0

while command != "END":
    command_to_lower = command.lower()
    if command_to_lower == "coding" or command_to_lower == "movie" \
            or command_to_lower == "cat" or command_to_lower == "dog":
        if command.isupper():
            count_of_coffee += 2
        else:
            count_of_coffee += 1

    command = input()
if count_of_coffee > 5:
    print("You need extra sleep")
else:
    print(f"{count_of_coffee}")
