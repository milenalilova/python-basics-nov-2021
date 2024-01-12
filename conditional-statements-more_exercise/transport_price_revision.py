km = int(input())
time_of_day = input()
price = 0

taxi_daily = 0.7 + 0.79 * km
taxi_night = 0.7 + 0.9 * km
bus = 0.09 * km
train = 0.06 * km

if km < 20:
    if time_of_day == 'day':
        price = taxi_daily
    elif time_of_day == 'night':
        price = taxi_night

elif 20 <= km < 100:
    if time_of_day == 'day':
        price = min(taxi_daily, bus)
    elif time_of_day == 'night':
        price = min(taxi_night, bus)

elif km >= 100:
    if time_of_day == 'day':
        price = min(taxi_daily, bus, train)
    elif time_of_day == 'night':
        price = min(taxi_night, bus, train)

print(f"{price:.2f}")
