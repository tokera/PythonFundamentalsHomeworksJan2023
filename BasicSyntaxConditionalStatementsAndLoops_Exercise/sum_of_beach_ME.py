text_string = input()

count_of_appearance = 0
text_string_to_lower = text_string.lower()

count_of_appearance += text_string_to_lower.count("water")
count_of_appearance += text_string_to_lower.count("sand")
count_of_appearance += text_string_to_lower.count("fish")
count_of_appearance += text_string_to_lower.count("sun")

print(count_of_appearance)
