days_off = int(input())

work_days = 365 - days_off
days_off_play_minutes = days_off * 127
work_days_play_minutes = work_days * 63
total_play_minuites = days_off_play_minutes + work_days_play_minutes
minites_left_to_play = 30000 - total_play_minuites

hours_left_to_play = abs(minites_left_to_play) // 60
minutes_left_to_play = abs(minites_left_to_play) % 60

if total_play_minuites > 30000:
    print("Tom will run away")
    print(f"{hours_left_to_play} hours and {minutes_left_to_play} minutes more for play")

else:
    print("Tom sleeps well")
    print(f"{hours_left_to_play} hours and {minutes_left_to_play} minutes less for play")
