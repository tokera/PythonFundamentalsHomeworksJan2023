numbers = input().split(", ")
beggars_count = int(input())

beggars = [0] * beggars_count

for i in range(len(numbers)):
    beggars_index = i % beggars_count
    num = int(numbers[i])
    beggars[beggars_index] += num

print(beggars)
