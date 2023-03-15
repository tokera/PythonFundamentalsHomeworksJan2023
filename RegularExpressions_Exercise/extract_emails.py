import re

text = input()

pattern = r"\b(((?<!\.)[a-z][a-z0-9\-\.\_]+)@[a-z\-]+(\.[a-z]+)+)\b"

result = re.findall(pattern, text)

[print(f"{x[0]}") for x in result]
