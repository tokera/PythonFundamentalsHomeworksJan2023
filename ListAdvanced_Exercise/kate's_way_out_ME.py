def find_start(matrix: list):
    coordinates = []
    for r in range(len(matrix)):
        if "k" in matrix[r]:
            coordinates.append(r)
            coordinates.append(matrix[r].index("k"))
            return coordinates

    return coordinates


def is_valid_position(matrix, r, c):
    if r < 0 or c < 0:
        return False
    elif r >= len(matrix) or c >= len(matrix[0]):
        return False
    return True


def find_possible_moves(current_maze, r, c):
    moves = []
    if r - 1 >= 0:
        moves.append([r - 1, c])

    if c - 1 >= 0:
        moves.append([r, c - 1])

    if r + 1 < len(current_maze):
        moves.append([r + 1, c])

    if c + 1 < len(current_maze[0]):
        moves.append([r, c + 1])

    return moves


rows = int(input())

maze = []

for _ in range(rows):
    row = input()
    maze.append([x for x in row])

initial_position = find_start(maze)
moves = [initial_position]

while moves:
    pass



