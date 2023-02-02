n = int(input())

for _ in range(n):
    text_string = input()

    # if text_string.__contains__(",") or text_string.__contains__(".") or text_string.__contains__("_"):
    #     print(f"{text_string} is not pure!")
    # else:
    #     print(f"{text_string} is pure.")

    for char in text_string:
        if char == "," or char == "." or char == "_":
            print(f"{text_string} is not pure!")
            break
    else:
        print(f"{text_string} is pure.")