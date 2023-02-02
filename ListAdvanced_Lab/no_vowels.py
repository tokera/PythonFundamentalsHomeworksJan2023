text = input()

vowels = ["a", "o", "u", "e", "i"]

text_without_vowels = [x for x in text if x.lower() not in vowels]

print("".join(text_without_vowels))
