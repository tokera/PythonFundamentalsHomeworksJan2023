init_energy = int(input())

current_energy = init_energy
wins = 0

command = input()
while command != "End of battle":
    distance = int(command)

    if current_energy - distance >= 0:
        current_energy -= distance
        wins += 1
    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {current_energy} energy")
        break
    if wins % 3 == 0:
        current_energy += wins

    command = input()
else:
    print(f"Won battles: {wins}. Energy left: {current_energy}")
