import random

computer_random_number = random.randint(1, 100)

while True:
    player_input = input("Guess a number in range (1 - 100): ")
    if not player_input.isdigit():
        print("Invalid Input! Try again...")
        continue

    guessed_number = int(player_input)

    if guessed_number == computer_random_number:
        print("You guess it!")
        break
    elif guessed_number > computer_random_number:
        print("Too High!")
    else:
        print("Too Low!")
