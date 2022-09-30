import math

tours_count = int(input())
initial_points = int(input())
points_won = 0
wins_count = 0

for tours in range(tours_count):
    round = input()
    if round == "W":
        points_won += 2000
        wins_count += 1
    elif round == "F":
        points_won += 1200
    elif round == "SF":
        points_won += 720

print(f"Final points: {initial_points + points_won}")
print(f"Average points: {math.floor(points_won / tours_count)}")
print(f"{wins_count / tours_count * 100:.2f}%")
