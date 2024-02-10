walk_minutes = int(input())
walks_count = int(input())
daily_calories = int(input())

calories_per_walk = walk_minutes * 5
calories_spent = walks_count * calories_per_walk

if calories_spent >= daily_calories / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_spent}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_spent}.")
