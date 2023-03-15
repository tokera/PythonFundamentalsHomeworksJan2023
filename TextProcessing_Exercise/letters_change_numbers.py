import string

input_words = input().split()
alphabet = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
result = []

for word in input_words:
    current_res = 0
    number = int(word[1:-1])
    if word[0].isupper():
        current_res += number / (alphabet_upper.index(word[0]) + 1)
    else:
        current_res += number * (alphabet.index(word[0]) + 1)

    if word[-1].isupper():
        current_res -= (alphabet_upper.index(word[-1]) + 1)
    else:
        current_res += (alphabet.index(word[-1]) + 1)

    result.append(current_res)

print(f"{(sum(result)):.2f}")
