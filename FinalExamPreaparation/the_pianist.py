n_of_pieces = int(input())

pieces_library = {}

for _ in range(n_of_pieces):
    piece, composer, key = input().split("|")

    if piece not in pieces_library:
        pieces_library[piece] = []

    pieces_library[piece].append(composer)
    pieces_library[piece].append(key)

command = input()
while command != "Stop":
    command_args = command.split("|")
    action = command_args[0]
    piece = command_args[1]

    if action == "Add":
        if piece in pieces_library:
            print(f"{piece} is already in the collection!")
        else:
            composer = command_args[2]
            key = command_args[3]
            pieces_library[piece] = []
            pieces_library[piece].append(composer)
            pieces_library[piece].append(key)
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif action == "Remove":
        if piece in pieces_library:
            pieces_library.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        if piece in pieces_library:
            new_key = command_args[2]
            pieces_library[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

[print(f"{piece} -> Composer: {info[0]}, Key: {info[1]}") for piece, info in pieces_library.items()]