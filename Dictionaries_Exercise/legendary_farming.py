valid_game = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
material_winner = ""
while True:
    line = input().split()

    for i in range(1, len(line), 2):
        material = line[i].lower()
        if material in valid_game:
            valid_game[material] += int(line[i - 1])

            if valid_game[material] >= 250:
                material_winner = material
                valid_game[material] -= 250
                break
        else:
            if material not in junk:
                junk[material] = int(line[i - 1])
            else:
                junk[material] += int(line[i - 1])
    if material_winner:
        break
winner = ""
if material_winner == "shards":
    winner = "Shadowmourne"
elif material_winner == "fragments":
    winner = "Valanyr"
elif material_winner == "motes":
    winner = "Dragonwrath"

print(f"{winner} obtained!")
[print(f"{mat}: {qty}") for mat, qty in valid_game.items()]
[print(f"{mat}: {qty}") for mat, qty in junk.items()]
