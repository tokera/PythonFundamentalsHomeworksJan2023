stack_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

count_of_racks = 1
clothes_in_current_rack = 0
flag_for_new_rack = False

while stack_of_clothes:
    if flag_for_new_rack:
        count_of_racks += 1
        clothes_in_current_rack = 0
        flag_for_new_rack = False

    current_cloth = stack_of_clothes.pop()
    clothes_in_current_rack += current_cloth

    if clothes_in_current_rack < rack_capacity:
        continue
    elif clothes_in_current_rack == rack_capacity:
        flag_for_new_rack = True
        continue

    count_of_racks += 1
    clothes_in_current_rack = current_cloth

print(count_of_racks)
