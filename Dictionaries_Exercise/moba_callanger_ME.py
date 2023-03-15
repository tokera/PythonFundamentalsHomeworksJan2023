players_by_positions = {}
players_by_total_points = {}

command_line = input()
while command_line != "Season end":
    if "->" in command_line:
        player, position, skill = command_line.split(" -> ")

        if player not in players_by_positions:
            players_by_positions[player] = {}

        if position not in players_by_positions[player]:
            players_by_positions[player][position] = int(skill)
        elif players_by_positions[player][position] < int(skill):
            players_by_positions[player][position] = int(skill)

    else:
        player_one, player_two = command_line.split(" vs ")

        if player_one in players_by_positions and player_two in players_by_positions:
            for position in players_by_positions[player_one]:
                if position in players_by_positions[player_two]:
                    total_points_player_one = sum(list(players_by_positions[player_one].values()))
                    total_points_player_two = sum(list(players_by_positions[player_two].values()))
                    if total_points_player_one > total_points_player_two:
                        players_by_positions.pop(player_two)
                        break
                    elif total_points_player_one < total_points_player_two:
                        players_by_positions.pop(player_one)
                        break

    command_line = input()

for player, positions in players_by_positions.items():
    players_by_total_points[player] = sum(list(players_by_positions[player].values()))

for player, total_points in sorted(players_by_total_points.items(), key=lambda x: (-x[1], x[0])):
    print(f"{player}: {total_points} skill")
    for position, skill in sorted(players_by_positions[player].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
