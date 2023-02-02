first_number = int(input())
second_number = int(input())
third_number = int(input())

list_of_nums = [first_number, second_number, third_number]

filtered_negatives = list(filter(lambda x: x < 0, list_of_nums))

if 0 in list_of_nums:
    print("zero")
elif len(filtered_negatives) % 2 == 0:
    print("positive")
else:
    print("negative")
