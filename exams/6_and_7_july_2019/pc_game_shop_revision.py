n = int(input())
hearthstone_qty = 0
fornite_qty = 0
overwatch_qty = 0
others_qty = 0

for game in range(n):
    game_name = input()

    if game_name == "Hearthstone":
        hearthstone_qty += 1
    elif game_name == "Fornite":
        fornite_qty += 1
    elif game_name == "Overwatch":
        overwatch_qty += 1
    else:
        others_qty += 1

total_games_count = hearthstone_qty + fornite_qty + overwatch_qty + others_qty

hearthstone_percentage = hearthstone_qty / total_games_count * 100
fornite_percentage = fornite_qty / total_games_count * 100
overwatch_percentage = overwatch_qty / total_games_count * 100
others_percentage = others_qty / total_games_count * 100

print(f"Hearthstone - {hearthstone_percentage:.2f}%")
print(f"Fornite - {fornite_percentage:.2f}%")
print(f"Overwatch - {overwatch_percentage:.2f}%")
print(f"Others - {others_percentage:.2f}%")
