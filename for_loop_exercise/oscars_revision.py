actors_name = input()
academy_points = float(input())
jury_count = int(input())

for jury in range(jury_count):
    jury_name = input()
    jury_points = float(input())

    actors_points = len(jury_name) * jury_points / 2
    academy_points += actors_points
    if academy_points >= 1250.5:
        print(f"Congratulations, {actors_name} got a nominee for leading role with {academy_points:.1f}!")
        break

if academy_points < 1250.5:
    diff = 1250.5 - academy_points
    print(f"Sorry, {actors_name} you need {diff:.1f} more!")
