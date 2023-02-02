numbers = list(map(int, input().split()))

numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(numbers)
