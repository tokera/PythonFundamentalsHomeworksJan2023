working_day_events = list(input().split("|"))

init_energy = 100
init_coins = 100

current_energy = init_energy
current_coins = init_coins

for event in working_day_events:
    event_to_list = list(event.split("-"))

    event_or_ingredient = event_to_list[0]
    number = int(event_to_list[1])

    if event_or_ingredient == "rest":
        gained_energy = 0
        if current_energy + number > init_energy:
            gained_energy = init_energy - current_energy
            current_energy = init_energy
        else:
            current_energy += number
            gained_energy = number

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")
    elif event_or_ingredient == "order":
        if current_energy - 30 >= 0:
            current_coins += number
            current_energy -= 30
            print(f"You earned {number} coins.")
        else:
            current_energy += 50
            print("You had to rest!")
    else:
        if current_coins - number >= 0:
            print(f"You bought {event_or_ingredient}.")
            current_coins -= number
        else:
            print(f"Closed! Cannot afford {event_or_ingredient}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")
