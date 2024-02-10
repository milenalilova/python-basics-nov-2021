from math import floor

record_sec = float(input())
distance_meters = float(input())
time_sec = float(input())

slowing_time = floor(distance_meters / 50) * 30

total_time = distance_meters * time_sec + slowing_time

if total_time < record_sec:
    print(f"Yes! The new record is {total_time:.2f} seconds.")

else:
    print(f"No! He was {total_time - record_sec:.2f} seconds slower.")
