days = int(input())
wins = 0
losses = 0
money_earned = 0
is_winner = False

for day in range(days):
    game = input()
    daily_wins = 0
    daily_losses = 0
    daily_money_earned = 0

    while game != "Finish":
        result = input()

        if result == "win":
            daily_wins += 1
            wins += 1
            daily_money_earned += 20

        elif result == "lose":
            daily_losses += 1
            losses += 1

        game = input()

    if daily_wins > daily_losses:
        daily_money_earned += daily_money_earned * 0.1
    money_earned += daily_money_earned

if wins > losses:
    is_winner = True
    money_earned += money_earned * 0.2

if is_winner:
    print(f"You won the tournament! Total raised money: {money_earned:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_earned:.2f}")
