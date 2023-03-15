first_string, second_string = input().split()

len_of_longer_string = max(len(first_string), len(second_string))
sum_of_letters = 0

for i in range(len_of_longer_string):
    if 0 <= i < len(first_string) and 0 <= i < len(second_string):
        sum_of_letters += ord(first_string[i]) * ord(second_string[i])
    elif 0 <= i < len(first_string):
        sum_of_letters += ord(first_string[i])
    elif 0 <= i < len(second_string):
        sum_of_letters += ord(second_string[i])

print(sum_of_letters)
