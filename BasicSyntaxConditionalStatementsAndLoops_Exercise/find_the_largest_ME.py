number = input()

result = []

for item in number:
    result.append(int(item))

result.sort(reverse=True)
print("".join(map(str, result)))
