command = input()

new_string = ""

while command != "End":
    if not command == "SoftUni":
        for char in command:
            for _ in range(2):
                new_string += char
        print(new_string)
        new_string = ""
    command = input()
