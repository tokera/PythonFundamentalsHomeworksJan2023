import re

text = input()

cool_threshold = 1
pattern = r"(?P<emoji>(:{2}|\*{2})(?P<text>[A-Z][a-z]{2,})(\2))"

matches = re.finditer(pattern, text)
digits_in_text = re.findall(r"\d", text)

for digit in digits_in_text:
    cool_threshold *= int(digit)

valid_emojis = [emoji.groupdict() for emoji in matches]

print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")

for emoji in valid_emojis:
    sum_ascii = 0
    for ch in emoji["text"]:
        sum_ascii += ord(ch)

    if sum_ascii >= cool_threshold:
        print(f"{emoji['emoji']}")
