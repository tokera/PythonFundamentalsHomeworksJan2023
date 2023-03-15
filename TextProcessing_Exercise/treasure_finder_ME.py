def find_word_between_symbols(seq, sym):
    word = ""
    sym_find = False

    for ch in seq:
        if sym_find:
            if ch == sym[1]:
                sym_find = False
                continue
            word += ch

        if ch == sym[0]:
            sym_find = True
            continue

    return word


key_sequence = [int(x) for x in input().split()]

text = input()

while text != "find":
    decrypted_msg = ""
    for i in range(len(text)):
        decrypted_msg += chr(ord(text[i]) - key_sequence[i % len(key_sequence)])

    type_of_treasure = find_word_between_symbols(decrypted_msg, ["&", "&"])
    coordinates = find_word_between_symbols(decrypted_msg, ["<", ">"])

    print(f"Found {type_of_treasure} at {coordinates}")

    text = input()
