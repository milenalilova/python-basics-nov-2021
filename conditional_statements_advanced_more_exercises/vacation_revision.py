budget = float(input())
season = input()

accommodation_type = ""
location = ""
accommodation_price = 0

if budget <= 1000:
    accommodation_type = "Camp"

    if season == "Summer":
        location = "Alaska"
        accommodation_price = budget * 0.65

    elif season == "Winter":
        location = "Morocco"
        accommodation_price = budget * 0.45

elif 1000 < budget <= 3000:
    accommodation_type = "Hut"

    if season == "Summer":
        location = "Alaska"
        accommodation_price = budget * 0.80

    elif season == "Winter":
        location = "Morocco"
        accommodation_price = budget * 0.60

elif budget > 3000:
    accommodation_type = "Hotel"
    accommodation_price = budget * 0.9

    if season == "Summer":
        location = "Alaska"

    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {accommodation_type} - {accommodation_price:.2f}")
