first_line = input().split()
second_line = input().split()
third_line = input().split()

board = [first_line, second_line, third_line]
winner = ""

for row in range(len(board)):
    if board[row][0] == board[row][1] == board[row][2]:
        winner = board[row][0]
        break
else:
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col]:
            winner = board[0][col]
            break
    else:
        if board[0][0] == board[1][1] == board[2][2]:
            winner = board[0][0]
        elif board[0][2] == board[1][1] == board[2][0]:
            winner = board[0][2]

if winner == "1":
    print("First player won")
elif winner == "2":
    print("Second player won")
else:
    print("Draw!")
