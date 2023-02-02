numbers = list(map(int, input().split(" ")))

for i in range(len(numbers)):
    numbers[i] *= -1

print(numbers)
