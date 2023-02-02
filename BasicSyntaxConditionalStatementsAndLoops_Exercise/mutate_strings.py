first_string = input()
second_string = input()

result_string = ""

for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        result_string = second_string[:i + 1] + first_string[i + 1:]
        print(result_string)
        result_string = ""
