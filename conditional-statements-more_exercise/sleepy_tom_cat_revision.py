days_off = int(input())
norm = 30000
working_days = 365 - days_off

playing_time = days_off * 127 + working_days * 63

difference = norm - playing_time

hours = abs(difference) // 60
minutes = abs(difference) % 60

if playing_time <= norm:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")

else:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
