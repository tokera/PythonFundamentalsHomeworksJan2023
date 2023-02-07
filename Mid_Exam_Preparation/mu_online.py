rooms = input().split("|")

initial_health = 100
current_health = 100
coins = 0

for room in rooms:
    room_args = room.split()
    command = room_args[0]
    number = int(room_args[1])

    if command == "potion":
        healed_for = number
        if current_health + number > initial_health:
            healed_for = initial_health - current_health
            current_health = initial_health
        else:
            current_health += number

        print(f"You healed for {healed_for} hp.")
        print(f"Current health: {current_health} hp.")
    elif command == "chest":
        print(f"You found {number} bitcoins.")
        coins += number
    else:
        current_health -= number

        if current_health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {rooms.index(room) + 1}")
            break
        else:
            print(f"You slayed {command}.")

else:
    print("You've made it!")
    print(f"Bitcoins: {coins}")
    print(f"Health: {current_health}")
