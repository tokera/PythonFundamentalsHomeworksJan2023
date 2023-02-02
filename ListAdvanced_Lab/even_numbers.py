numbers = list(map(int, input().split(", ")))

find_indices_or_no = map(lambda x: x if numbers[x] % 2 == 0 else "no", range(len(numbers)))

even_indices = list(filter(lambda x: not x == "no", find_indices_or_no))
print(even_indices)
