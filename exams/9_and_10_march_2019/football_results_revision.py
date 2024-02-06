team_lost = 0
team_won = 0
team_drawn = 0

for i in range(3):
    result = input()

    host_result = int(result[0])
    guest_result = int(result[2])

    if host_result > guest_result:
        team_won += 1
    elif host_result == guest_result:
        team_drawn += 1
    elif host_result < guest_result:
        team_lost += 1

print(f"Team won {team_won} games.")
print(f"Team lost {team_lost} games.")
print(f"Drawn games: {team_drawn}")
