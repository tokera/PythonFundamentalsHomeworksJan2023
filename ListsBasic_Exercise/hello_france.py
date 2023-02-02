items_with_price = list(input().split("|"))
budget = float(input())

item_prices = []
is_item_below_max_price = False

for item in items_with_price:
    item_to_list = list(item.split("->"))
    item_type = item_to_list[0]
    item_price = float(item_to_list[1])

    if item_type == "Clothes":
        if item_price <= 50:
            is_item_below_max_price = True
    elif item_type == "Shoes":
        if item_price <= 35:
            is_item_below_max_price = True
    elif item_type == "Accessories":
        if item_price <= 20.5:
            is_item_below_max_price = True

    if budget - ((sum(item_prices)) + item_price) >= 0:
        if is_item_below_max_price:
            item_prices.append(item_price)
            is_item_below_max_price = False

money_before_sell_items = sum(item_prices)

for idx in range(len(item_prices)):
    item_prices[idx] += item_prices[idx] * (40 / 100)
    if idx == len(item_prices) - 1:
        print(f"{item_prices[idx]:.2f}")
    else:
        print(f"{item_prices[idx]:.2f}", end=" ")

profit = sum(item_prices) - money_before_sell_items
print(f"Profit: {profit:.2f}")

if budget + profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
