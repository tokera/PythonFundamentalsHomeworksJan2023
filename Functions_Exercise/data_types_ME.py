type_input = input()
data_input = input()


def solve(type_of_var, data):

    if type_of_var == "int":
        return int(data) * 2
    elif type_of_var == "real":
        return f"{(float(data) * 1.5):.2f}"
    elif type_of_var == "string":
        return "$" + data + "$"


print(solve(type_input, data_input))
