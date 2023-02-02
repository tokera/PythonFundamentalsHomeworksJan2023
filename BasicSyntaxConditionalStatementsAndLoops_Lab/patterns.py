num = int(input())

for i in range(1, num + 1):
    for j in range(i):
        print('*', end='')
    print()
for k in range(num - 1, 0, -1):
    for y in range(k):
        print('*', end='')
    print()
