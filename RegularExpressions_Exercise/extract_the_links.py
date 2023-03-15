import re

text = input()
pattern = r"(www\.([A-Za-z0-9\-])+(\.[a-z]+)+)\b"

while text:
    result = re.findall(pattern, text)

    for item in result:
        print(result[0][0])

    text = input()
