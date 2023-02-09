array_of_ints = [int(x) for x in input().split()]

command = input()

while command != "end":
    command_args = command.split()
    cmd = command_args[0]

    if cmd == "swap":
        index_1 = int(command_args[1])
        index_2 = int(command_args[2])
        array_of_ints[index_1], array_of_ints[index_2] = array_of_ints[index_2], array_of_ints[index_1]
    elif cmd == "multiply":
        index_1 = int(command_args[1])
        index_2 = int(command_args[2])
        array_of_ints[index_1] *= array_of_ints[index_2]
    else:
        array_of_ints = [x - 1 for x in array_of_ints]

    command = input()

print(", ".join([str(x) for x in array_of_ints]))
