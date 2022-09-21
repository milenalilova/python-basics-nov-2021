vegi_price = float(input())
fruit_price = float(input())
vegi_in_kilos = float(input())
fruit_in_kilos = float(input())
sales_in_leva = vegi_in_kilos * vegi_price + fruit_in_kilos * fruit_price
euro = 1.94
sales_in_euro = sales_in_leva / euro
print(f"{sales_in_euro:.2f}")
