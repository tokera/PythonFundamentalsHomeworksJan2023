words = input().split()

words_dict = {}

for word in words:
    lower_word = word.lower()
    if lower_word not in words_dict:
        words_dict[lower_word] = 1
        continue
    words_dict[lower_word] += 1

[print(f"{word}", end=" ") for word, occurrence in words_dict.items() if occurrence % 2 != 0]
