from math import floor

tours_count = int(input())
starting_points = int(input())
wins = 0
points = 0
final_points = starting_points + points

for tour in range(tours_count):
    position = input()

    if position == "W":
        points = 2000
        final_points += points
        wins += 1

    elif position == "F":
        points = 1200
        final_points += points

    elif position == "SF":
        points = 720
        final_points += points

average_points = (final_points - starting_points) / tours_count
percentage_wins = wins / tours_count * 100

print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percentage_wins:.2f}%")
