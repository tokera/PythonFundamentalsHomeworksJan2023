def is_valid_index(idx, seq):
    if 0 <= idx < len(seq):
        return True
    return False


sequence = input().split()

counter_of_moves = 0
indices = input()
while indices != "end":
    counter_of_moves += 1
    indices_args = indices.split()
    first_idx = int(indices_args[0])
    second_idx = int(indices_args[1])

    if not is_valid_index(first_idx, sequence) or not is_valid_index(second_idx, sequence) or first_idx == second_idx:
        half = len(sequence) // 2
        sequence.insert(half, f"-{counter_of_moves}a")
        sequence.insert(half, f"-{counter_of_moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif sequence[first_idx] == sequence[second_idx]:
        element = sequence[first_idx]
        sequence = [x for x in sequence if x != element]
        print(f"Congrats! You have found matching elements - {element}!")
    else:
        print("Try again!")

    if not sequence:
        print(f"You have won in {counter_of_moves} turns!")
        break

    indices = input()
else:
    print("Sorry you lose :(")
    print(" ".join(sequence))
