estate = float(input())
year_to_live = int(input())
money_spent = 0
age = 18

for year in range(1800, year_to_live + 1):
    if year % 2 == 0:
        money_spent += 12000

    else:
        money_spent += 12000 + 50 * age

    age += 1

diff = abs(estate - money_spent)

if estate >= money_spent:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")

else:
    print(f"He will need {diff:.2f} dollars to survive.")
