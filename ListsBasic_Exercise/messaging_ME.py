numbers = input().split()
text = input()

for n in numbers:
    sum_of_digits = 0
    for digit in n:
        sum_of_digits += int(digit)

    if sum_of_digits >= len(text):
        sum_of_digits %= len(text)

    print(text[sum_of_digits], end="")
    text = text[:sum_of_digits] + text[sum_of_digits + 1:]
