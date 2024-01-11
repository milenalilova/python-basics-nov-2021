from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())

slowing_times = floor(distance_in_meters / 15)
slowing_seconds = slowing_times * 12.5
time_for_distance = distance_in_meters * time_in_seconds + slowing_seconds

if time_for_distance < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {time_for_distance:.2f} seconds.")
else:
    print(f"No, he failed! He was {(time_for_distance - record_in_seconds):.2f} seconds slower.")
