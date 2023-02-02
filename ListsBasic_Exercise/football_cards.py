cards = list(input().split(" "))

team_A = 11
team_B = 11
sent_off_players_A = []
sent_off_players_B = []
game_terminated = False

for card in cards:

    card_list = list(card.split("-"))

    if card_list[0] == "A":
        if not sent_off_players_A.__contains__(card_list[1]):
            team_A -= 1
            sent_off_players_A.append(card_list[1])

    elif card_list[0] == "B":
        if not sent_off_players_B.__contains__(card_list[1]):
            team_B -= 1
            sent_off_players_B.append(card_list[1])

    if team_A < 7 or team_B < 7:
        game_terminated = True
        break

print(f"Team A - {team_A}; Team B - {team_B}")

if game_terminated:
    print("Game was terminated")
