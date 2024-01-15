budget = float(input())
ticket_type = input()
people_count = int(input())
transport_cost = 0
ticket_cost = 0

if 1 <= people_count <= 4:
    transport_cost = budget * 0.75

elif 5 <= people_count <= 9:
    transport_cost = budget * 0.6

elif 10 <= people_count <= 24:
    transport_cost = budget * 0.5

elif 25 <= people_count <= 49:
    transport_cost = budget * 0.4

elif people_count > 50:
    transport_cost = budget * 0.25

budget_left = budget - transport_cost

if ticket_type == "VIP":
    ticket_cost = people_count * 499.99

elif ticket_type == "Normal":
    ticket_cost = people_count * 249.99

money_left = abs(budget_left - ticket_cost)

if budget_left >= ticket_cost:
    print(f"Yes! You have {money_left:.2f} leva left.")

else:
    print(f"Not enough money! You need {money_left:.2f} leva.")
