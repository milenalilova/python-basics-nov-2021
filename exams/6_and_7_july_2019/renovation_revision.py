from math import ceil

width = int(input())
length = int(input())
percentage_non_painted = int(input())
walls_area = width * length * 4
walls_area -= walls_area * percentage_non_painted / 100
all_walls_painted = False

command = input()
while command != "Tired!":
    paint_lt = int(command)
    walls_area -= paint_lt

    if walls_area <= 0:
        all_walls_painted = True
        break

    command = input()

if not all_walls_painted:
    print(f"{ceil(walls_area)} quadratic m left.")
else:
    if walls_area == 0:
        print("All walls are painted! Great job, Pesho!")
    elif walls_area < 0:
        print(f"All walls are painted and you have {abs(ceil(walls_area))} l paint left!")
