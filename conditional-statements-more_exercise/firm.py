import math

hours_needed = int(input())
days = int(input())
people_working_extra = int(input())

days_left = days - days * 0.1
hours_left = days_left * 8
extra_hours = people_working_extra * days * 2
total_hours_for_project = math.floor(hours_left + extra_hours)

if total_hours_for_project >= hours_needed:
    print(f'Yes!{total_hours_for_project - hours_needed} hours left.')
else:
    print(f"Not enough time!{hours_needed - total_hours_for_project} hours needed.")
