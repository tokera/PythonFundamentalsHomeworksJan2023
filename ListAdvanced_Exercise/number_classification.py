numbers = list(map(int, input().split(", ")))

positives = [x for x in numbers if x >= 0]
negatives = [x for x in numbers if x < 0]
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if not x % 2 == 0]

print("Positive: ", end="")
print(", ".join(map(str, positives)))
print("Negative: ", end="")
print(", ".join(map(str, negatives)))
print("Even: ", end="")
print(", ".join(map(str, even)))
print("Odd: ", end="")
print(", ".join(map(str, odd)))
