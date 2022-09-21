mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())
bonito_price = mackerel_price + mackerel_price * 0.6
horse_mackerel_price = sprat_price + sprat_price * 0.8
mussles_price = 7.5

bill = bonito_kg * bonito_price + horse_mackerel_kg * horse_mackerel_price + mussels_kg * mussles_price
print(f"{bill:.2f}")
