sequence = [int(x) for x in input().split()]

average = sum(sequence) / len(sequence)

nums_greater_then_average = [x for x in sequence if x > average]

result = sorted(nums_greater_then_average, reverse=True)[:5]

if result:
    print(" ".join(str(x) for x in result))
else:
    print("No")
