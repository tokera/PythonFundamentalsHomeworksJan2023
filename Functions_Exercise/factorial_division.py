import math

first_num = int(input())
second_num = int(input())


def calculate_factorial_division(first, second):
    return math.factorial(first) / math.factorial(second)


print(f"{calculate_factorial_division(first_num, second_num):.2f}")
