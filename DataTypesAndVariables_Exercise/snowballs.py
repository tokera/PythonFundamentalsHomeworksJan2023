count_of_snowballs = int(input())

max_snowball_value = 0
max_weight = 0
max_time = 0
max_quality = 0

for snowball in range(count_of_snowballs):
    weight = int(input())
    time_to_target = int(input())
    quality = int(input())

    current_snowball_value = (weight / time_to_target) ** quality

    if current_snowball_value > max_snowball_value:
        max_snowball_value = current_snowball_value
        max_weight = weight
        max_time = time_to_target
        max_quality = quality

print(f"{max_weight} : {max_time} = {int(max_snowball_value)} ({max_quality})")
