days = int(input())
accommodation = input()
review = input()
price = 0
nights = days - 1

if accommodation == "room for one person":
    price = 18

elif accommodation == "apartment":
    if days < 10:
        price = 25 - 25 * 0.3

    elif 10 <= days <= 15:
        price = 25 - 25 * 0.35

    elif days > 15:
        price = 25 - 25 * 0.5

elif accommodation == "president apartment":
    if days < 10:
        price = 35 - 35 * 0.1

    elif 10 <= days <= 15:
        price = 35 - 35 * 0.15

    elif days > 15:
        price = 35 - 35 * 0.2

accommodation_cost = nights * price

if review == "positive":
    accommodation_cost += accommodation_cost * 0.25

elif review == "negative":
    accommodation_cost -= accommodation_cost * 0.1

print(f"{accommodation_cost:.2f}")
