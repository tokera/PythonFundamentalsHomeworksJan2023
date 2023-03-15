import re

pattern = r"%([A-Z][a-z]+)\%([^|$%.]+)?\<(\w+)\>([^|$%.]+)?\|(\d+)\|.*?(\d+(\.\d+)?(?=\$))"
command = input()
total_price = 0

while command != "end of shift":
    result = re.findall(pattern, command)

    if result:
        name = result[0][0]
        product = result[0][2]
        price = int(result[0][4]) * float(result[0][-2])
        total_price += price

        print(f"{name}: {product} - {price:.2f}")

    command = input()

print(f"Total income: {total_price:.2f}")
