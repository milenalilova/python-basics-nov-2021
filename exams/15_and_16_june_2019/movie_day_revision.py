time_amount = int(input())
scene_count = int(input())
time_per_scene = int(input())

preparation_time = time_amount * 0.15

time_needed = preparation_time + scene_count * time_per_scene

if time_amount >= time_needed:
    print(f"You managed to finish the movie on time! You have {round(time_amount-time_needed)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(time_needed-time_amount)} minutes.")
