input_string = input()

list_of_strings = [str(x) for x in input_string]

numbers_list = [x for x in list_of_strings if x.isdigit()]
non_numbers_list = [x for x in list_of_strings if not x.isdigit()]
take_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 == 0]
skip_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 != 0]

result = []
current_index = 0

for i in range(len(take_list)):
    take = int(take_list[i])
    skip = int(skip_list[i])

    result.extend(non_numbers_list[current_index:current_index + take])
    current_index += take + skip

print("".join(result))
