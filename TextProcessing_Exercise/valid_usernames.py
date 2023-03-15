usernames = input().split(", ")

for username in usernames:
    if not 3 <= len(username) <= 16:
        continue

    for letter in username:
        if not letter.isalnum() and letter != "-" and letter != "_":
            break
    else:
        print(username)
