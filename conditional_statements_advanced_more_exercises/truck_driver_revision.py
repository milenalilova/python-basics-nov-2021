season = input()
monthly_km = float(input())

price_per_km = 0
season_payment = 0

if season == "Spring" or season == "Autumn":
    if monthly_km <= 5000:
        price_per_km = 0.75

    elif 5000 < monthly_km <= 10000:
        price_per_km = 0.95

    elif 10000 < monthly_km <= 20000:
        price_per_km = 1.45

elif season == "Summer":
    if monthly_km <= 5000:
        price_per_km = 0.90

    elif 5000 < monthly_km <= 10000:
        price_per_km = 1.10

    elif 10000 < monthly_km <= 20000:
        price_per_km = 1.45

elif season == "Winter":
    if monthly_km <= 5000:
        price_per_km = 1.05

    elif 5000 < monthly_km <= 10000:
        price_per_km = 1.25

    elif 10000 < monthly_km <= 20000:
        price_per_km = 1.45

season_payment = monthly_km * 4 * price_per_km
net_salary = season_payment - season_payment * 0.10

print(f"{net_salary:.2f}")
