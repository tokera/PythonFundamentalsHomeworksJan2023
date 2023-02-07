def find_initial_coordinates(matrix: list):
    coordinates = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "k":
                coordinates.append(r)
                coordinates.append(c)
                return coordinates


def is_valid_position(matrix, r, c):
    if r < 0 or c < 0:
        return False
    elif r >= len(matrix) or c > len(matrix[0]):
        return False
    elif matrix[r][c] == "#":
        return False

    return True


rows = int(input())

maze = []

for _ in range(rows):
    row = input()
    maze.append([x for x in row])

initial_position = find_initial_coordinates(maze)
movies = [initial_position]

while movies:
    current_r, current_c = movies.pop()

    if current_r == 0 or current_c == 0 or current_r == len(maze) or current_c == len(maze[0]):
        break
    if maze[current_r][current_c] == "x":
        continue

    if is_valid_position(maze, current_r, current_c + 1):
        movies.append([current_r, current_c + 1])
        maze[current_r][current_c + 1] = "x"
    if is_valid_position(maze, current_r, current_c - 1):
        movies.append([current_r, current_c - 1])
        maze[current_r][current_c - 1] = "x"
    if is_valid_position(maze, current_r + 1, current_c):
        movies.append([current_r + 1, current_c])
        maze[current_r + 1][current_c] = "x"
    if is_valid_position(maze, current_r - 1, current_c):
        movies.append([current_r - 1, current_c])
        maze[current_r - 1][current_c] = "x"




