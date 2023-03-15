class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_latter: str):
        filtered = [x for x in self.products if x[0].startswith(first_latter)]
        return filtered

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:"
        self.products.sort()
        for product in self.products:
            result += f"\n{product}"
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
