control_minutes = int(input())
control_seconds = int(input())
length_meters = float(input())
seconds_for_hundred_meters = int(input())

control_time = control_minutes * 60 + control_seconds
time_needed = length_meters / 100 * seconds_for_hundred_meters
time_decrease = length_meters / 120 * 2.5
time_needed -= time_decrease

if time_needed <= control_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_needed:.3f}.")
else:
    print(f"No, Marin failed! He was {abs(control_time - time_needed):.3f} second slower.")
