n = int(input())

brackets = ""
is_balanced = True

for _ in range(n):
    read_input = input()

    if read_input == "(":
        brackets += read_input
    elif read_input == ")":
        brackets += read_input

for i in range(len(brackets)):
    if i % 2 == 0 and brackets[i] == "(":
        continue
    elif i % 2 != 0 and brackets[i] == ")":
        continue
    else:
        is_balanced = False


if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
