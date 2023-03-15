text = input()
result = ""
last_char = ""

for ch in text:
    if ch != last_char:
        last_char = ch
        result += last_char

print(result)
