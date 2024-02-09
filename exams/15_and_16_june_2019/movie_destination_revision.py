budget = float(input())
destination = input()
season = input()
days_count = int(input())
daily_cost = 0

if destination == "Dubai":
    if season == "Winter":
        daily_cost = 45000

    elif season == "Summer":
        daily_cost = 40000
    daily_cost -= daily_cost * 0.3

elif destination == "Sofia":
    if season == "Winter":
        daily_cost = 17000

    elif season == "Summer":
        daily_cost = 12500
    daily_cost += daily_cost * 0.25


elif destination == "London":
    if season == "Winter":
        daily_cost = 24000

    elif season == "Summer":
        daily_cost = 20250

total_cost = days_count * daily_cost

if budget >= total_cost:
    print(f"The budget for the movie is enough! We have {budget - total_cost:.2f} leva left!")
else:
    print(f"The director needs {total_cost - budget:.2f} leva more!")
