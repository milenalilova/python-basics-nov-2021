vacation_cost = float(input())
saved_money = float(input())

spend_times = 0
days_passed = 0
has_saved = False

while spend_times < 5:
    action = input()
    amount = float(input())

    if action == "spend":
        spend_times += 1
        if amount <= saved_money:
            saved_money -= amount
        else:
            saved_money = 0

    elif action == "save":
        saved_money += amount
        spend_times = 0

    days_passed += 1

    if saved_money >= vacation_cost:
        has_saved = True
        break

if not has_saved:
    print("You can't save the money.")
    print(days_passed)
else:
    print(f"You saved the money for {days_passed} days.")
