n = int(input())

stack = []

for _ in range(n):
    query = input()

    if query.startswith("1"):
        query_args = query.split()
        num = int(query_args[1])
        stack.append(num)
    elif stack:
        if query == "2":
            stack.pop()
        elif query == "3":
            print(max(stack))
        elif query == "4":
            print(min(stack))

result = []

while stack:
    result.append(stack.pop())

print(*result, sep=", ")

