input_product = input()
quantity = int(input())


def calculate_price(product, qty):
    price = 0

    if product == "coffee":
        price = 1.5
    elif product == "coke":
        price = 1.4
    elif product == "water":
        price = 1.0
    elif product == "snacks":
        price = 2.0

    return f"{(price * qty):.2f}"


print(calculate_price(input_product, quantity))
