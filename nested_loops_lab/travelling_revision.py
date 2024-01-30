destination = input()
saved_money = 0

while destination != "End":
    budget = float(input())
    while saved_money < budget:
        earned_money = float(input())
        saved_money += earned_money
        if saved_money >= budget:
            print(f"Going to {destination}!")

    destination = input()
    saved_money = 0
