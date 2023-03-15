line = input()
products = {}
while line != "buy":
    name, price, qty = line.split()

    if name not in products:
        products[name] = []
        products[name].append(float(price))
        products[name].append(int(qty))
    else:
        products[name][0] = float(price)
        products[name][1] += int(qty)

    line = input()

[print(f"{product} -> {(info[0] * info[1]):.2f}") for product, info in products.items()]
