import re

count_of_messages = int(input())

pattern = r"[star]"

for _ in range(count_of_messages):
    message = input()

    result = re.findall(pattern, message, re.IGNORECASE)

    decrypted_message = ""
    for ch in message:
        decrypted_message += chr(ord(ch) - len(result))

    planet_name = re.search(r"(?<=\@)([A-Za-z]+)", decrypted_message)
    print(planet_name.group())