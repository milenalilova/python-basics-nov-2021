# actor_name = input()
# academy_points = float(input())
# judges_number = int(input())
# actor_points = 0
#
# for judge in range(1, judges_number + 1):
#     judge_name = input()
#     judge_points = float(input())
#     actor_points += (len(judge_name) * judge_points) / 2
#
#     if academy_points + actor_points > 1250.5:
#         print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points + actor_points:.1f}!")
#         break
# if academy_points + actor_points <= 1250.5:
#     print(f"Sorry, {actor_name} you need {1250.50 - (academy_points + actor_points):.1f} more!")


actor_name = input()
initial_points = float(input())
judges_number = int(input())

points_needed = 1250.5
# is_nominated = False

for judge in range(1, judges_number + 1):
    judge_name = input()
    judge_points = float(input())
    initial_points += (len(judge_name) * judge_points) / 2

    if initial_points > points_needed:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {initial_points:.1f}!")
        # is_nominated == True
        break
if initial_points < points_needed:  # if not is_nominated:
    print(f"Sorry, {actor_name} you need {points_needed - initial_points:.1f} more!")
