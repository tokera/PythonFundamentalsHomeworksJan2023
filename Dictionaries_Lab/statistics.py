bakery = {}

line = input()
while line != "statistics":
    command = line.split(": ")
    key = command[0]
    value = int(command[1])

    if key not in bakery:
        bakery[key] = 0

    bakery[key] += value

    line = input()

print("Products in stock:")

# for item in bakery:
#     print(f"- {item}: {bakery[item]}")

[print(f"- {product}: {quantity}") for (product, quantity) in bakery.items()]

print(f"Total Products: {len(bakery)}")
print(f"Total Quantity: {sum(bakery.values())}")
