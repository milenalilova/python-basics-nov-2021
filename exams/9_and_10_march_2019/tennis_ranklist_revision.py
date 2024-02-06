from math import floor

tours_count = int(input())
initial_points = int(input())
points_won=0
tours_won = 0

for tour in range(tours_count):
    round_type = input()

    if round_type == "W":
        points_won += 2000
        tours_won += 1

    elif round_type == "F":
        points_won += 1200

    elif round_type == "SF":
        points_won += 720

final_points = initial_points+points_won
average_points = points_won / tours_count
tours_won_percentage = tours_won / tours_count * 100

print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f"{tours_won_percentage:.2f}%")
