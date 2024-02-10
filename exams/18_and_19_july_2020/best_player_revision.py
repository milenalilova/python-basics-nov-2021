name = input()
max_goals = 0
best_player = ''

while name != "END":
    goals = int(input())
    if goals > max_goals:
        max_goals = goals
        best_player = name
        if goals >= 10:
            break

    name = input()

print(f"{best_player} is the best player!")

if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
