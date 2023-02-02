first_number = int(input())
second_number = int(input())
third_number = int(input())


def find_smallest(f_num, s_num, t_num):
    list_of_numbers = [f_num, s_num, t_num]

    return min(list_of_numbers)


print(find_smallest(first_number, second_number, third_number))
