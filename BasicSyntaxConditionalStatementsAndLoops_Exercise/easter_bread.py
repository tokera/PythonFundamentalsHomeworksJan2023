budget = float(input())
price_for_one_kg_flour = float(input())

price_for_one_pack_eggs = price_for_one_kg_flour * (75 / 100)
price_for_litter_milk = price_for_one_kg_flour + (price_for_one_kg_flour * (25 / 100))

price_for_one_loaf = price_for_one_kg_flour + price_for_one_pack_eggs + (price_for_litter_milk / 4)
counter = 0
colored_eggs = 0
count_of_loaves = 0

while True:
    if budget - price_for_one_loaf >= 0:
        budget -= price_for_one_loaf
        colored_eggs += 3
        count_of_loaves += 1
        counter += 1

        if counter % 3 == 0:
            colored_eggs -= count_of_loaves - 2

    else:
        break

print(f"You made {count_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
