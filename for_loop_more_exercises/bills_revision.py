months = int(input())

electricity_cost = 0
other_cost = 0

for month in range(1, months + 1):
    electricity_bill = float(input())
    electricity_cost += electricity_bill
    other_cost += (electricity_bill + 20 + 15) + (electricity_bill + 20 + 15) * 0.2

water_cost = months * 20
internet_cost = months * 15
average_cost = (electricity_cost + water_cost + internet_cost + other_cost) / months

print(f"Electricity: {electricity_cost:.2f} lv")
print(f"Water: {water_cost:.2f} lv")
print(f"Internet: {internet_cost:.2f} lv")
print(f"Other: {other_cost:.2f} lv")
print(f"Average: {average_cost:.2f} lv")
