expression = input()

stack = []

for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(i)
    elif expression[i] == ")":
        start_idx = stack.pop()
        print(expression[start_idx:i + 1])
