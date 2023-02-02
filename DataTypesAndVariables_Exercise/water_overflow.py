n = int(input())

tank_capacity = 255
liters_in_tank = 0

for _ in range(n):
    liters_of_water = int(input())

    if (liters_in_tank + liters_of_water) > tank_capacity:
        print("Insufficient capacity!")
        continue
    else:
        liters_in_tank += liters_of_water

print(f"{liters_in_tank}")
