days = int(input())
hours = int(input())

total_price = 0

for day in range(1, days + 1):
    daily_price = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0:
            if hour % 2 != 0:
                daily_price += 2.5
            else:
                daily_price += 1
        else:
            if hour % 2 == 0:
                daily_price += 1.25
            else:
                daily_price += 1
    print(f"Day: {day} - {daily_price:.2f} leva")
    total_price += daily_price

print(f"Total: {total_price:.2f} leva")
