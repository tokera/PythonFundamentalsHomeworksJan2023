import re

pattern = r"\d+"
text = input()

while text:
    result = re.findall(pattern, text)

    if result:
        print(" ".join(result), end=" ")

    text = input()
