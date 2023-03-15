products_in_bakery = input().split()

products_as_dictionary = {}

for i in range(0, len(products_in_bakery), 2):
    key = products_in_bakery[i]
    value = products_in_bakery[i + 1]

    products_as_dictionary[key] = int(value)

print(products_as_dictionary)
