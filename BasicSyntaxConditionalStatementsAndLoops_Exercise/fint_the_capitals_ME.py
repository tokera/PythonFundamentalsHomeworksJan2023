text_string = input()

indices = []

for index in range(len(text_string)):
    if text_string[index].isupper():
        indices.append(index)

print(indices)
