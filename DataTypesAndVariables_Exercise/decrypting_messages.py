key = int(input())
n_of_lines = int(input())

decrypted_message = ""

for _ in range(n_of_lines):
    letter = input()

    decrypted_message += chr(ord(letter) + key)

print(decrypted_message)
