# First solution

# from math import ceil
#
# seq_of_numbers = list(map(int, input().split(", ")))
#
# max_boundary = ceil((max(seq_of_numbers) / 10)) * 10
#
# for i in range(10, max_boundary + 1, 10):
#     print(f"Group of {i}'s: {list(filter(lambda x: i - 10 < x <= i, seq_of_numbers))}")


# Second solution

seq_of_numbers = list(map(int, input().split(", ")))
initial_boundary = 10

while seq_of_numbers:
    current_group = list(filter(lambda x: x <= initial_boundary, seq_of_numbers))

    seq_of_numbers = [x for x in seq_of_numbers if x not in current_group]

    print(f"Group of {initial_boundary}'s: {current_group}")
    initial_boundary += 10
