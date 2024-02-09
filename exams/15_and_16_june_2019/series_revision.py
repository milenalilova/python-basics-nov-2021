budget = float(input())
series_count = int(input())
series_cost = 0

for series in range(series_count):
    series_name = input()
    series_price = float(input())

    if series_name == "Thrones":
        series_price -= series_price * 0.5

    elif series_name == "Lucifer":
        series_price -= series_price * 0.4

    elif series_name == "Protector":
        series_price -= series_price * 0.3

    elif series_name == "TotalDrama":
        series_price -= series_price * 0.2

    elif series_name == "Area":
        series_price -= series_price * 0.1

    series_cost += series_price

if budget >= series_cost:
    print(f"You bought all the series and left with {budget - series_cost:.2f} lv.")
else:
    print(f"You need {series_cost - budget:.2f} lv. more to buy the series!")
