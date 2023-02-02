number = input()


def calculate_even_and_odd_sum(num):
    odd_sum = sum(int(i) for i in num if int(i) % 2 != 0)
    even_sum = sum(int(i) for i in num if int(i) % 2 == 0)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


print(calculate_even_and_odd_sum(number))
