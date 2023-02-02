fires_and_cells = list(input().split("#"))
water = int(input())

effort = 0
total_fire = 0
cells_put_out = []
is_valid_value_of_cell = False

for idx in range(len(fires_and_cells)):
    current_fire = list(fires_and_cells[idx].split(" = "))
    type_of_fire = current_fire[0]
    value_of_cell = int(current_fire[1])

    if type_of_fire == "High" and 81 <= value_of_cell <= 125:
        is_valid_value_of_cell = True
    elif type_of_fire == "Medium" and 51 <= value_of_cell <= 80:
        is_valid_value_of_cell = True
    elif type_of_fire == "Low" and 1 <= value_of_cell <= 50:
        is_valid_value_of_cell = True

    if is_valid_value_of_cell:
        if water - value_of_cell < 0:
            continue

        water -= value_of_cell
        effort += value_of_cell * (25 / 100)
        cells_put_out.append(value_of_cell)
        total_fire += value_of_cell
        is_valid_value_of_cell = False

print("Cells:")

for cell in cells_put_out:
    print(f" - {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
