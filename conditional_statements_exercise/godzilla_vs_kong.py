budget = float(input())
extra_number = int(input())
single_clothes_price = float(input())

decor = budget * 0.1
total_clothes_cost = single_clothes_price * extra_number

if extra_number > 150:
    total_clothes_cost = total_clothes_cost - (total_clothes_cost * 0.1)

final_movie_cost = decor + total_clothes_cost
budget_left = budget - final_movie_cost

if final_movie_cost > budget:
    print("Not enough money!")
    print(f'Wingard needs {abs(budget_left):.2f} leva more.')

else:
    print("Action!")
    print(f'Wingard starts filming with {budget_left:.2f} leva left.')
