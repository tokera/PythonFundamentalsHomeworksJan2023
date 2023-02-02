start = int(input())
stop = int(input())

for num in range(start, stop + 1):
    print(f"{chr(num)}", end=" ")
