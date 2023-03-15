text = input()

current_word = ""
result = ""
number_of_repeating = ""

for i in range(len(text)):
    if text[i].isdigit():
        number_of_repeating += text[i]
        if i == len(text) - 1:
            result += current_word.upper() * int(number_of_repeating)
    elif number_of_repeating:
        result += current_word.upper() * int(number_of_repeating)
        current_word = ""
        number_of_repeating = ""
        current_word += text[i]
    else:
        current_word += text[i]

unique_symbols = set(result)

print(f"Unique symbols used: {len(unique_symbols)}")
print(result, end="")
