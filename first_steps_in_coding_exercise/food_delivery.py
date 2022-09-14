chicken_menu_price = 10.35
fish_menu_price = 12.40
veg_menu_price = 8.15

number_chicken_menu = int(input())
number_fish_menu = int(input())
number_veg_menu = int(input())

order_price = chicken_menu_price*number_chicken_menu + fish_menu_price*number_fish_menu + \
              veg_menu_price*number_veg_menu
dessert_price = order_price*0.2
total_order_price = order_price + dessert_price + 2.5

print(total_order_price)
