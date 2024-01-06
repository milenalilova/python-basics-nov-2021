chicken_menu_price = 10.35
fish_menu_price = 12.4
vegetarian_menu_price = 8.15
delivery_price = 2.5

chicken_menu_quantity = int(input())
fish_menu_quantity = int(input())
vegetarian_menu_quantity = int(input())

menus_cost = chicken_menu_quantity * chicken_menu_price + fish_menu_quantity * fish_menu_price + vegetarian_menu_quantity * vegetarian_menu_price
desert_cost = menus_cost * 0.2

order_cost = menus_cost + desert_cost + delivery_price

print(order_cost)
