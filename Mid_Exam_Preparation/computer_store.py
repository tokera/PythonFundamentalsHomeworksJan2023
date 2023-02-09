price = input()

price_without_taxes = 0
taxes = 0
total_price = 0

while price != "special" and price != "regular":
    price_as_a_num = float(price)

    if price_as_a_num < 0:
        print("Invalid price!")
        price = input()
        continue

    price_without_taxes += price_as_a_num
    taxes += price_as_a_num * (20 / 100)

    price = input()

total_price = price_without_taxes + taxes
if total_price == 0:
    print("Invalid order!")
    exit(0)

if price == "special":
    total_price -= total_price * (10 / 100)

print("Congratulations you've just bought a new computer!")
print(f"Price without taxes: {price_without_taxes:.2f}$")
print(f"Taxes: {taxes:.2f}$")
print("-----------")
print(f"Total price: {total_price:.2f}$")
