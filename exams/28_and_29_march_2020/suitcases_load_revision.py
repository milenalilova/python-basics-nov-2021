hold_capacity = float(input())
no_capacity = False
suitcase_counter = 0
suitcases_loaded = 0

command = input()

while command != "End":
    volume = float(command)
    suitcase_counter += 1
    if suitcase_counter % 3 == 0:
        volume += volume * 0.1

    if volume > hold_capacity:
        no_capacity = True
        break
    else:
        hold_capacity -= volume
        suitcases_loaded += 1

    command = input()

if not no_capacity:
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")

print(f"Statistic: {suitcases_loaded} suitcases loaded.")
