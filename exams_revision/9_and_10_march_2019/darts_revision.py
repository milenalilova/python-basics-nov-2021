name = input()
points = 301
successful_shots = 0
unsuccessful_shots = 0

command = input()

while command != "Retire":

    current_points = int(input())

    if command == "Single":
        current_points = current_points

    elif command == "Double":
        current_points = current_points * 2

    elif command == "Triple":
        current_points = current_points * 3

    if current_points <= points:
        points -= current_points
        successful_shots += 1

    else:
        unsuccessful_shots += 1

    if points == 0:
        break

    command = input()

if points == 0:
    print(f"{name} won the leg with {successful_shots} shots.")

else:
    print(f"{name} retired after {unsuccessful_shots} unsuccessful shots.")
