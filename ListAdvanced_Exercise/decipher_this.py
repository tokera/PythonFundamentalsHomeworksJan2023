secret_messages = input().split()

deciphered_message = []

for word in secret_messages:
    list_of_letters = [*word]
    first_letter = ""
    counter = 0

    for letter in list_of_letters:
        if letter.isdigit():
            first_letter += letter
            counter += 1

    list_of_letters[counter], list_of_letters[-1] = list_of_letters[-1], list_of_letters[counter]

    deciphered_word = chr(int(first_letter)) + "".join(list_of_letters[counter:])
    deciphered_message.append(deciphered_word)

print(" ".join(deciphered_message))
