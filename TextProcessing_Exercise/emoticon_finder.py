text = input()

emoticon = ""

for ch in text:
    if emoticon:
        if ch != " ":
            emoticon += ch
            print(emoticon)
            emoticon = ""
    if ch == ":":
        emoticon += ch
