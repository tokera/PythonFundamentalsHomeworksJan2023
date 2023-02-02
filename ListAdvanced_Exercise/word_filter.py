list_of_text = input().split()

#result = [x for x in list_of_text if len(x) % 2 == 0]
result = list(filter(lambda x: len(x) % 2 == 0, list_of_text))

print("\n".join(result))
