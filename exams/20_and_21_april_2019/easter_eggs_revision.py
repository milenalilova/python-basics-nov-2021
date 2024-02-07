import sys

eggs_count = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_colour = ""

for egg in range(eggs_count):

    egg_colour = input()

    if egg_colour == "red":
        red_eggs += 1
    elif egg_colour == "orange":
        orange_eggs += 1
    elif egg_colour == "blue":
        blue_eggs += 1
    elif egg_colour == "green":
        green_eggs += 1

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")

max_eggs = max(red_eggs, orange_eggs, blue_eggs, green_eggs)

if max_eggs == red_eggs:
    max_colour = "red"
elif max_eggs == orange_eggs:
    max_colour = "orange"
elif max_eggs == blue_eggs:
    max_colour = "blue"
elif max_eggs == green_eggs:
    max_colour = "green"

print(f"Max eggs: {max_eggs} -> {max_colour}")
