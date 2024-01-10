time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = total_time // 60
seconds = total_time - minutes * 60
if seconds <= 9:
    seconds = f"0{seconds}"

print(f"{minutes}:{seconds}")
