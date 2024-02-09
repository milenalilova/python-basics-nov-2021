team_name = input()
games_played = int(input())

w_count = 0
d_count = 0
l_count = 0
points = 0

for game in range(games_played):
    result = input()

    if result == "W":
        points += 3
        w_count += 1

    elif result == "D":
        points += 1
        d_count += 1

    elif result == "L":
        l_count += 1

if games_played == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    win_percentage = w_count / games_played * 100

    print(f"{team_name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {w_count}")
    print(f"## D: {d_count}")
    print(f"## L: {l_count}")
    print(f"Win rate: {win_percentage:.2f}%")
