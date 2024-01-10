holiday_cost = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

number_toys = number_puzzles + number_dolls + number_bears + number_minions + number_trucks

puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

order_cost = number_puzzles * puzzle_price + number_dolls * doll_price + number_bears * bear_price + \
             number_minions * minion_price + number_trucks * truck_price

if number_toys >= 50:
    order_cost = order_cost - 0.25 * order_cost

rent = order_cost * 0.1

profit = order_cost - rent

if profit >= holiday_cost:
    money_left = profit - holiday_cost
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = holiday_cost - profit
    print(f"Not enough money! {money_needed:.2f} lv needed.")
