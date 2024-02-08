budget = float(input())
fuel_ltr = float(input())
day = input()

fuel_cost = fuel_ltr * 2.10
tour_guide_cost = 100

total_cost = fuel_cost + tour_guide_cost

if day == "Saturday":
    total_cost -= total_cost * 0.10

elif day == "Sunday":
    total_cost -= total_cost * 0.20

if budget >= total_cost:
    print(f"Safari time! Money left: {budget-total_cost:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {total_cost-budget:.2f} lv.")
