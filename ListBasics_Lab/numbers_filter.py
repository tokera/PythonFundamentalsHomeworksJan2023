n_lines = int(input())

numbers = []

for _ in range(n_lines):
    number = int(input())

    numbers.append(number)

command = input()

if command == "even":
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
elif command == "odd":
    numbers = list(filter(lambda x: not x % 2 == 0, numbers))
elif command == "negative":
    numbers = list(filter(lambda x: x < 0, numbers))
elif command == "positive":
    numbers = list(filter(lambda x: x >= 0, numbers))

print(numbers)
