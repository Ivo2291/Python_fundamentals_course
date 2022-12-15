teams_info = input().split(" ")

a_team_players = 11
b_team_players = 11
players_lost = []
game_was_terminated = False

for card in teams_info:
    if card not in players_lost:
        players_lost.append(card)

        if "A" in card:
            a_team_players -= 1
        else:
            b_team_players -= 1

        if a_team_players < 7 or b_team_players < 7:
            game_was_terminated = True
            break

print(f"Team A - {a_team_players}; Team B - {b_team_players}")
if game_was_terminated:
    print("Game was terminated")

# second_solution

a_team = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
b_team = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
sent_off_players = input().split()
referee_stops_the_game = False

for player in sent_off_players:
    if player in a_team:
        a_team.remove(player)
    elif player in b_team:
        b_team.remove(player)
    if len(a_team) < 7 or len(b_team) < 7:
        referee_stops_the_game = True
        break

print(f"Team A - {len(a_team)}; Team B - {len(b_team)}")

if referee_stops_the_game:
    print("Game was terminated")
