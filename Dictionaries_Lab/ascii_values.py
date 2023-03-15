characters = input().split(", ")

result = {key: ord(key) for key in characters}

print(result)
