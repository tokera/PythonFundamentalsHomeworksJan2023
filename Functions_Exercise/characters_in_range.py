def find_characters_in_range(f_char, s_char):
    res = ""

    for ch in range(ord(f_char) + 1, ord(s_char)):
        res += chr(ch) + " "

    return res


first_char = input()
second_char = input()

print(find_characters_in_range(first_char, second_char))
