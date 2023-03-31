parentheses = input()

stack = []
open_parentheses = {"{": "}", "[": "]", "(": ")"}
start_with_closing_parent = False

for parent in parentheses:
    if parent in open_parentheses:
        stack.append(parent)
        continue
    elif stack:
        last_parent = stack.pop()
        if parent == open_parentheses[last_parent]:
            continue
        else:
            stack.append(last_parent)
    else:
        start_with_closing_parent = True

if stack or start_with_closing_parent:
    print("NO")
else:
    print("YES")
