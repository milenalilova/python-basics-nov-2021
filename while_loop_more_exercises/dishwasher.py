bottles_count = int(input())

liquid_ml = bottles_count * 750
liquid_needed = 0
plates_count = 0
pots_count = 0
counter = 1

is_not_enough = False

command = input()

# While True could be used as well

while liquid_ml >= 0:
    if command == "End":
        break

    dishes_count = int(command)

    if counter % 3 == 0:
        pots_count += dishes_count
        liquid_needed = dishes_count * 15
        if liquid_needed <= liquid_ml:
            liquid_ml -= liquid_needed
        else:
            is_not_enough = True
            break
    else:
        plates_count += dishes_count
        liquid_needed = dishes_count * 5
        if liquid_needed <= liquid_ml:
            liquid_ml -= liquid_needed
        else:
            is_not_enough = True
            break

    counter += 1

    command = input()

if not is_not_enough:
    print("Detergent was enough!")
    print(f"{plates_count} dishes and {pots_count} pots were washed.")
    print(f"Leftover detergent {liquid_ml} ml.")

else:
    print(f"Not enough detergent, {liquid_needed-liquid_ml} ml. more necessary!")
