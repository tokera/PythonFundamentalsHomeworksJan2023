n = int(input())

sum_of_ascii_chars = 0

for _ in range(n):
    char = input()
    sum_of_ascii_chars += ord(char)

print(f"The sum equals: {sum_of_ascii_chars}")
