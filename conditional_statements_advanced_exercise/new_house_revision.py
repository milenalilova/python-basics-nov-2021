flower = input()
flower_count = int(input())
budget = int(input())
price = 0

if flower == "Roses":
    price = 5
    if flower_count > 80:
        price -= price * 0.1

elif flower == "Dahlias":
    price = 3.8
    if flower_count > 90:
        price -= price * 0.15

elif flower == "Tulips":
    price = 2.8
    if flower_count > 80:
        price -= price * 0.15

elif flower == "Narcissus":
    price = 3
    if flower_count < 120:
        price += price * 0.15

elif flower == "Gladiolus":
    price = 2.5
    if flower_count < 80:
        price += price * 0.2

flower_cost = flower_count * price
difference = abs(budget - flower_cost)

if budget >= flower_cost:
    print(f"Hey, you have a great garden with {flower_count} {flower} and {difference:.2f} leva left.")

else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
