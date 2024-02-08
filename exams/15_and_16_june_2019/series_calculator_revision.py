from math import ceil
series_name = input()
seasons_count = int(input())
episodes_count = int(input())
episodes_length = float(input())

advertising_time = episodes_length * 0.2 * episodes_count
total_minutes = ((episodes_count - 1) * episodes_length + episodes_length + 10 + advertising_time) * seasons_count

print(f"Total time needed to watch the {series_name} series is {ceil(total_minutes)} minutes.")
