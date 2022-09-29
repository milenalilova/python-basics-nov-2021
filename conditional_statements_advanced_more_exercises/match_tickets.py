budget = float(input())
category = input()
people_count = int(input())
vip_ticket = 499.99
normal_ticket = 249.99

transport = 0
ticket_cost = 0

if 1 <= people_count <= 4:
    transport = budget * 0.75
elif 5 <= people_count <= 9:
    transport = budget * 0.6
elif 10 <= people_count <= 24:
    transport = budget * 0.5
elif 25 <= people_count <= 49:
    transport = budget * 0.4
elif people_count >= 50:
    transport = budget * 0.25

money_left = budget - transport

if category == "VIP":
    ticket_cost = people_count * vip_ticket
elif category == "Normal":
    ticket_cost = people_count * normal_ticket
if money_left >= ticket_cost:
    print(f"Yes! You have {money_left - ticket_cost:.2f} leva left.")
else:
    print(f'Not enough money! You need {ticket_cost - money_left:.2f} leva.')
