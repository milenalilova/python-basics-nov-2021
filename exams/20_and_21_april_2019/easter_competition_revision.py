import sys

easter_bread_count = int(input())

max_points = -sys.maxsize
max_name = ''

for easter_bread in range(easter_bread_count):
    points = 0
    baker_name = input()
    command = input()
    while command != "Stop":
        note = int(command)
        points += note

        command = input()

    print(f"{baker_name} has {points} points.")
    if points > max_points:
        max_points = points
        max_name = baker_name
        print(f"{baker_name} is the new number 1!")
print(f"{max_name} won competition with {max_points} points!")
