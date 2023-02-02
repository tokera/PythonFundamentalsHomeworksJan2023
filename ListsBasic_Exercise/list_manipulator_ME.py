initial_numbers = list(map(int, input().split()))
command = input()

while command != "end":
    command_as_list = command.split()

    if command_as_list[0] == "exchange":
        index = int(command_as_list[1])
        if index < 0 or index >= len(initial_numbers):
            print("Invalid index")
        else:
            tmp = initial_numbers[index + 1:] + initial_numbers[:index + 1]
            initial_numbers = tmp
    elif command_as_list[0] == "max":
        tmp = []
        if command_as_list[1] == "even":
            tmp = list(filter(lambda x: x % 2 == 0, initial_numbers))
        elif command_as_list[1] == "odd":
            tmp = list(filter(lambda x: not x % 2 == 0, initial_numbers))

        if tmp:
            initial_numbers.reverse()
            print((len(initial_numbers) - 1) - initial_numbers.index(max(tmp)))
            initial_numbers.reverse()
        else:
            print("No matches")
    elif command_as_list[0] == "min":
        tmp = []
        if command_as_list[1] == "even":
            tmp = list(filter(lambda x: x % 2 == 0, initial_numbers))
        elif command_as_list[1] == "odd":
            tmp = list(filter(lambda x: not x % 2 == 0, initial_numbers))

        if tmp:
            initial_numbers.reverse()
            print((len(initial_numbers) - 1) - initial_numbers.index(min(tmp)))
            initial_numbers.reverse()
        else:
            print("No matches")
    elif command_as_list[0] == "first":
        count = int(command_as_list[1])
        filtered_numbers = []
        if count > len(initial_numbers) or count < 0:
            print("Invalid count")
        else:
            if command_as_list[2] == "even":
                filtered_numbers = list(filter(lambda x: x % 2 == 0, initial_numbers))
            else:
                filtered_numbers = list(filter(lambda x: not x % 2 == 0, initial_numbers))
            print(filtered_numbers[:count])
    elif command_as_list[0] == "last":
        count = int(command_as_list[1])
        filtered_numbers = []
        if count > len(initial_numbers) or count < 0:
            print("Invalid count")
        else:
            if command_as_list[2] == "even":
                filtered_numbers = list(filter(lambda x: x % 2 == 0, initial_numbers[::-1]))
            else:
                filtered_numbers = list(filter(lambda x: not x % 2 == 0, initial_numbers[::-1]))
            filtered_numbers.reverse()

            if count > len(filtered_numbers):
                print(filtered_numbers)
            else:
                print(filtered_numbers[len(filtered_numbers) - count:])
    command = input()

print(initial_numbers)
