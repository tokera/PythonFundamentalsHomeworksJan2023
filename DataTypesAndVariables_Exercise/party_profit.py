group_size = int(input())
days = int(input())

profit = 0

for day in range(1, days + 1):

    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    profit += 50
    profit -= (group_size * 2)

    if day % 3 == 0:
        profit -= (group_size * 3)

    if day % 5 == 0:
        profit += (group_size * 20)

        if day % 3 == 0:
            profit -= (group_size * 2)

print(f"{group_size} companions received {int(profit / group_size)} coins each.")
