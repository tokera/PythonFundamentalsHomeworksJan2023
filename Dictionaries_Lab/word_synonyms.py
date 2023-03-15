count_of_words = int(input())

dictionary = {}
for _ in range(count_of_words):
    word = input()
    synonym = input()

    if word not in dictionary:
        dictionary[word] = []

    dictionary[word].append(synonym)

[print(f"{word} - {', '.join(synonyms)}") for word, synonyms in dictionary.items()]
