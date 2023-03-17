import re

text = input()

mirror_words = []
pattern = r"([@#])(?P<first>[A-Za-z]{3,})(\1){2}(?P<second>[A-Za-z]{3,})(\1)"
regex_pattern = re.compile(pattern)

if regex_pattern.search(text) is None:
    print("No word pairs found!")
else:
    matching_pairs = regex_pattern.finditer(text)

    counter = 0
    for pair in matching_pairs:
        counter += 1
        first_word = pair.group("first")
        second_word = pair.group("second")
        if first_word == second_word[::-1]:
            mirror_words.append(first_word + " <=> " + second_word)
    print(f"{counter} word pairs found!")
if mirror_words:
    print("The mirror words are:")
    print(*mirror_words, sep=", ")
else:
    print("No mirror words!")
