from math import ceil

series_name = str(input())
series_run_time = int(input())
break_time = int(input())

lunch_time = break_time * 0.125
leisure_time = break_time * 0.25
time_left = break_time - lunch_time - leisure_time

if time_left >= series_run_time:
    print(f'You have enough time to watch {series_name} and left with {ceil(time_left - series_run_time)} '
          f'minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(series_run_time - time_left)}"
          f" more minutes.")
