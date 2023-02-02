n = int(input())
word = input()

list_of_strings = []

for _ in range(n):
    text = input()
    list_of_strings.append(text)

print(list_of_strings)

list_of_strings = list(filter(lambda txt: word in txt, list_of_strings))

print(list_of_strings)
