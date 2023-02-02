numbers = list(map(int, input().split()))
count_of_numbers_to_remove = int(input())

for _ in range(count_of_numbers_to_remove):
    numbers.remove(min(numbers))

print(", ".join(map(str, numbers)))
