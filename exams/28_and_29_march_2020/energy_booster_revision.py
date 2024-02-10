fruit = input()
set_type = input()
sets_count = int(input())
set_price = 0

if fruit == "Watermelon":
    if set_type == "small":
        set_price = 56 * 2

    elif set_type == "big":
        set_price = 28.70 * 5

elif fruit == "Mango":
    if set_type == "small":
        set_price = 36.66 * 2

    elif set_type == "big":
        set_price = 19.60 * 5

elif fruit == "Pineapple":
    if set_type == "small":
        set_price = 42.10 * 2

    elif set_type == "big":
        set_price = 24.80 * 5

elif fruit == "Raspberry":
    if set_type == "small":
        set_price = 20 * 2

    elif set_type == "big":
        set_price = 15.20 * 5

order_cost = sets_count * set_price

if 400 <= order_cost <= 1000:
    order_cost -= order_cost * 0.15
elif order_cost > 1000:
    order_cost -= order_cost * 0.50

print(f"{order_cost:.2f} lv.")
