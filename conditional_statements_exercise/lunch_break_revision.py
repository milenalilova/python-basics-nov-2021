from math import ceil

show_name = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
rest_time = break_length / 4
free_time = break_length - lunch_time - rest_time

difference = free_time - episode_length

if difference >= 0:
    print(f"You have enough time to watch {show_name} and left with {ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {show_name}, you need {ceil(abs(difference))} more minutes.")
