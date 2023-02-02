numbers = list(map(int, input().split(", ")))

zeros = []

for n in numbers:
    if n == 0:
        zeros.append(n)

numbers = list(filter(lambda x: x != 0, numbers))
numbers += zeros

print(numbers)
