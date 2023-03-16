n_of_lines = int(input())
plants = {}
plants_by_rating = {}

for _ in range(n_of_lines):
    plant, rarity = input().split("<->")
    plants[plant] = int(rarity)

command = input()
while command != "Exhibition":
    command_args = command.split(": ")
    action = command_args[0]
    if action == "Rate":
        plant, rate = command_args[1].split(" - ")
        if plant not in plants:
            print("error")
        else:
            if plant not in plants_by_rating:
                plants_by_rating[plant] = []
            plants_by_rating[plant].append(int(rate))
    elif action == "Update":
        plant, rarity = command_args[1].split(" - ")
        if plant not in plants:
            print("error")
        else:
            plants[plant] = rarity
    elif action == "Reset":
        plant = command_args[1]
        if plant not in plants_by_rating:
            print("error")
        else:
            plants_by_rating.pop(plant)

    command = input()

print("Plants for the exhibition:")

for plant in plants:
    rating = 0
    if plant in plants_by_rating:
        rating = sum(plants_by_rating[plant]) / len(plants_by_rating[plant])
    print(f"- {plant}; Rarity: {plants[plant]}; Rating: {rating:.2f}")
