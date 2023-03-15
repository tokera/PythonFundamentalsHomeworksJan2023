n = int(input())

dragons = {}
types_by_averages = {}

for _ in range(n):
    type_of_dragon, name, damage, health, armor = [int(x) if x.isdigit() else x for x in input().split()]

    if damage == "null":
        damage = 45

    if health == "null":
        health = 250

    if armor == "null":
        armor = 10

    if type_of_dragon not in dragons:
        dragons[type_of_dragon] = {}

    if name not in dragons[type_of_dragon]:
        dragons[type_of_dragon][name] = []
        dragons[type_of_dragon][name].extend([damage, health, armor])
    else:
        dragons[type_of_dragon][name][0] = damage
        dragons[type_of_dragon][name][1] = health
        dragons[type_of_dragon][name][2] = armor

for type_of_dragon, names in dragons.items():
    types_by_averages[type_of_dragon] = []
    av_damage = 0
    av_health = 0
    av_armor = 0
    count_of_dragons = 0
    for name, stats in names.items():
        av_damage += stats[0]
        av_health += stats[1]
        av_armor += stats[2]
        count_of_dragons += 1

    types_by_averages[type_of_dragon].append(av_damage / count_of_dragons)
    types_by_averages[type_of_dragon].append(av_health / count_of_dragons)
    types_by_averages[type_of_dragon].append(av_armor / count_of_dragons)

for type_of_dragon, names in dragons.items():
    print(f"{type_of_dragon}::({(types_by_averages[type_of_dragon][0]):.2f}/"
          f"{(types_by_averages[type_of_dragon][1]):.2f}/{(types_by_averages[type_of_dragon][2]):.2f})")
    for name, stats in sorted(dragons[type_of_dragon].items(), key=lambda x: (x[0], x[1])):
        print(f"-{name} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}")
