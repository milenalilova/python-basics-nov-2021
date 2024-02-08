budget = float(input())

product_name = input()
products_count = 0
products_bought = 0
products_cost = 0
is_not_enough = False

while product_name != "Stop":

    product_price = float(input())
    products_count += 1

    if products_count % 3 == 0:
        product_price /= 2

    if budget < product_price:
        is_not_enough = True
        print("You don't have enough money!")
        print(f"You need {product_price - budget:.2f} leva!")
        break

    budget -= product_price
    products_cost += product_price
    products_bought += 1

    product_name = input()

if not is_not_enough:
    print(f"You bought {products_bought} products for {products_cost:.2f} leva.")
