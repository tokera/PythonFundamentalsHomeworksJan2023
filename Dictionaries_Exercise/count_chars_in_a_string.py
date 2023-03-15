text = input()

text_as_dictionary = {}

for ch in text:
    if ch == " ":
        continue

    if ch not in text_as_dictionary:
        text_as_dictionary[ch] = 1
    else:
        text_as_dictionary[ch] += 1

[print(f"{ch} -> {occurrence}") for ch, occurrence in text_as_dictionary.items()]
