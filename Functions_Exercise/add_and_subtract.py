def add_and_subtract(f_num, s_num, t_num):
    def sum_numbers(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    return subtract(sum_numbers(f_num, s_num), t_num)


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
