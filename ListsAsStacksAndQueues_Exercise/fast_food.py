from collections import deque

food_quantity = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))
while orders:
    current_order = orders.popleft()

    if current_order <= food_quantity:
        food_quantity -= current_order
        continue

    print(f"Orders left: {current_order} {' '.join([str(x) for x in orders])}")
    break
else:
    print("Orders complete")
