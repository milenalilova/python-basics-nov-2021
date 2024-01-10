number = int(input())
bonus_points = 0
additional_points = 0

if number % 2 == 0:
    additional_points = 1

if number % 10 == 5:
    additional_points = 2

if number <= 100:
    bonus_points = 5

elif 100 < number <= 1000:
    bonus_points = number * 0.2

elif number > 1000:
    bonus_points = number * 0.1

all_points = bonus_points + additional_points
total_points = number + all_points

print(all_points)
print(total_points)
