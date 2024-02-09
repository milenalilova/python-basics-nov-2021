actors_name = input()
academy_points = float(input())
jury_count = int(input())
is_nominated = False
# actors_points = 0

for i in range(jury_count):
    jury_name = input()
    jury_points = float(input())

    actors_points = (len(jury_name) * jury_points) / 2
    academy_points += actors_points

    if academy_points > 1250.5:
        is_nominated = True
        break

if is_nominated:
    print(f"Congratulations, {actors_name} got a nominee for leading role with {academy_points:.1f}!")
else:
    print(f"Sorry, {actors_name} you need {1250.5 - academy_points:.1f} more!")

