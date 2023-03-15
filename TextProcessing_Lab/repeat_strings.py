input_string = input().split()

for word in input_string:
    # for _ in range(len(word)):
    #     print(word, end="")
    print(word * len(word), end="")
