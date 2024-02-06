tour_name = input()
wins = 0
losses = 0
total_games = 0

while tour_name != "End of tournaments":
    games_count = int(input())
    total_games += games_count

    for game in range(1, games_count + 1):
        desi_team_points = int(input())
        other_team_points = int(input())

        if desi_team_points > other_team_points:
            print(f"Game {game} of tournament {tour_name}: win with {desi_team_points - other_team_points} points.")
            wins += 1
        elif other_team_points > desi_team_points:
            print(f"Game {game} of tournament {tour_name}: lost with {other_team_points - desi_team_points} points.")
            losses += 1

    tour_name = input()

wins_percentage = wins / total_games * 100
losses_percentage = losses / total_games * 100

print(f"{wins_percentage:.2f}% matches win")
print(f"{losses_percentage:.2f}% matches lost")
