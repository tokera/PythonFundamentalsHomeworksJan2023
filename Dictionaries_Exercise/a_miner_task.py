command = input()
line_counter = 0
mine_products = {}
resource = ""
while command != "stop":
    line_counter += 1
    if line_counter % 2 != 0:
        resource = command
        if resource not in mine_products:
            mine_products[resource] = 0
    else:
        mine_products[resource] += int(command)

    command = input()

[print(f"{src} -> {qty}") for src, qty in mine_products.items()]
