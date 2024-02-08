contract_duration = input()
contract_type = input()
internet_added = input()
months_count = int(input())
monthly_tax = 0
internet_cost = 0

if contract_duration == "one":

    if contract_type == "Small":
        monthly_tax = 9.98

    elif contract_type == "Middle":
        monthly_tax = 18.99

    elif contract_type == "Large":
        monthly_tax = 25.98

    elif contract_type == "ExtraLarge":
        monthly_tax = 35.99

elif contract_duration == "two":

    if contract_type == "Small":
        monthly_tax = 8.58

    elif contract_type == "Middle":
        monthly_tax = 17.09

    elif contract_type == "Large":
        monthly_tax = 23.59

    elif contract_type == "ExtraLarge":
        monthly_tax = 31.79

total_price = monthly_tax * months_count

if internet_added == "yes":
    if monthly_tax <= 10:
        internet_cost = 5.50

    elif 10 < monthly_tax <= 30:
        internet_cost = 4.35

    elif monthly_tax > 30:
        internet_cost = 3.85

total_price += internet_cost * months_count

if contract_duration == "two":
    total_price -= total_price * 0.0375

print(f"{total_price:.2f} lv.")
