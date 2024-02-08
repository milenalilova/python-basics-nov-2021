days_count = int(input())
hours_count = int(input())

# hourly_price = 0
daily_price = 0
total_price = 0

for day in range(1, days_count + 1):
    for hour in range(1, hours_count + 1):
        if day % 2 == 0 and hour % 2 != 0:
            hourly_price = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            hourly_price = 1.25
        else:
            hourly_price = 1

        daily_price += hourly_price
    total_price += daily_price

    print(f"Day: {day} - {daily_price:.2f} leva")
    daily_price = 0

print(f"Total: {total_price:.2f} leva")
