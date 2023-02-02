input_data = input().split()
command = input().split()


def manipulate_input_data(f_part, s_part, t_part):
    res = f_part
    if type(s_part) == str:
        res.append(s_part)
    else:
        res += s_part
    res += t_part

    return res


while command[0] != "3:1":
    if command[0] == "merge":
        start_idx = int(command[1])
        end_idx = int(command[2])
        merged_data = ""

        if start_idx < 0:
            start_idx = 0

        if end_idx >= len(input_data):
            end_idx = len(input_data) - 1

        for i in range(start_idx, end_idx + 1):
            merged_data += input_data[i]

        input_data = manipulate_input_data(input_data[:start_idx], merged_data, input_data[end_idx + 1:])

    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])
        divided_cell = input_data[index]
        divided_data = []

        n = len(divided_cell) // partitions

        if not len(divided_cell) % partitions == 0:
            partitions -= 1

        current_part = 1

        for i in range(0, len(divided_cell), n):
            if current_part <= partitions:
                divided_data.append(divided_cell[i:i + n])
            else:
                divided_data.append(divided_cell[i:])
                break
            current_part += 1

        input_data = manipulate_input_data(input_data[:index], divided_data, input_data[index + 1:])

    command = input().split()

print(" ".join(input_data))
