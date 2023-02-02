operation = input()
first_number = int(input())
second_number = int(input())


def calculate(calc_operation, a, b):
    res = 0

    if calc_operation == "multiply":
        res = a * b
    elif calc_operation == "divide":
        res = int(a / b)
    elif calc_operation == "add":
        res = a + b
    elif calc_operation == "subtract":
        res = a - b

    return res


print(calculate(operation, first_number, second_number))
