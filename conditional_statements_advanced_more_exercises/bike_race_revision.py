juniors_count = int(input())
seniors_count = int(input())
route_type = input()

group_count = juniors_count + seniors_count
juniors_tax = 0
seniors_tax = 0

if route_type == "trail":
    juniors_tax = 5.5
    seniors_tax = 7

elif route_type == "cross-country":
    juniors_tax = 8
    seniors_tax = 9.5

elif route_type == "downhill":
    juniors_tax = 12.25
    seniors_tax = 13.75

elif route_type == "road":
    juniors_tax = 20
    seniors_tax = 21.5

group_tax = juniors_count * juniors_tax + seniors_count * seniors_tax

if group_count >= 50:
    group_tax -= group_tax * 0.25

expenses = group_tax * 0.05

sum_left = group_tax - expenses

print(f"{sum_left:.2f}")
