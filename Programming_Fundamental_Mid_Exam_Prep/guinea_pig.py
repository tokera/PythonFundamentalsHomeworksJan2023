food_for_month = float(input())
hay_for_month = float(input())
cover_for_month = float(input())
pig_weight = float(input())

food_for_month_in_g = food_for_month * 1000
hay_for_month_in_g = hay_for_month * 1000
cover_for_month_in_g = cover_for_month * 1000
pig_weight_in_g = pig_weight * 1000
days = 0

while days < 30:
    days += 1
    food_for_month_in_g -= 300

    if days % 2 == 0:
        hay_for_month_in_g -= food_for_month_in_g * (5 / 100)

    if days % 3 == 0:
        cover_for_month_in_g -= pig_weight_in_g / 3

    if food_for_month_in_g <= 0 or hay_for_month_in_g <= 0 or cover_for_month_in_g <= 0:
        print("Merry must go to the pet store!")
        break
else:
    print(f"Everything is fine! Puppy is happy! Food: "
          f"{food_for_month_in_g / 1000:.2f}, "
          f"Hay: {hay_for_month_in_g / 1000:.2f}, "
          f"Cover: {cover_for_month_in_g / 1000:.2f}.")
