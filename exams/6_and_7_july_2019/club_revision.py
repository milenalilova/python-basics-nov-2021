profit_target = float(input())
sales = 0

cocktail_name = input()

while cocktail_name != "Party!":
    cocktail_count = int(input())
    cocktail_price = len(cocktail_name)
    order_cost = cocktail_price * cocktail_count

    if order_cost % 2 != 0:
        order_cost -= order_cost * 0.25
    sales += order_cost

    if sales >= profit_target:
        break

    cocktail_name = input()

if profit_target > sales:
    print(f"We need {profit_target - sales:.2f} leva more.")

else:
    print("Target acquired.")

print(f"Club income - {sales:.2f} leva.")
