budget = float(input())

command = input()

no_budget = False
diff = 0

while command != "ACTION":
    actors_name = command
    if len(actors_name) > 15:
        actors_pay = budget * 0.2
    else:
        actors_pay = float(input())

    if budget < actors_pay:
        diff = actors_pay - budget
        no_budget = True
        break

    budget -= actors_pay

    command = input()

if not no_budget:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {diff:.2f} leva for our actors.")
