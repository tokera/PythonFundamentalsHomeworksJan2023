numbers = list(map(float, input().split()))

for i in range(len(numbers)):
    numbers[i] = round(numbers[i])

print(numbers)
