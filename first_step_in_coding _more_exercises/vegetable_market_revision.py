veg_price = float(input())
fruit_price = float(input())
veg_kg = float(input())
fruit_kg = float(input())
lv_to_euro_rate = 1.94

income_lv = veg_kg * veg_price + fruit_kg * fruit_price
income_euro = income_lv / lv_to_euro_rate

print(f"{income_euro:.2f}")
