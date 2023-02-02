numbers = list(map(int, input().split(", ")))
beggars = int(input())

result = []

for beggar in range(beggars):
    current_sum = 0
    for i in range(beggar, len(numbers), beggars):
        current_sum += numbers[i]

    result.append(current_sum)

print(result)
