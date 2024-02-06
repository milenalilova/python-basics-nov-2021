first_name = input()
second_name = input()
first_name_points = 0
second_name_points = 0
is_number_wars = False
is_winner = ""

command = input()

while command != "End of game":
    first_card = int(command)
    second_card = int(input())

    if first_card > second_card:
        first_name_points += first_card - second_card

    elif second_card > first_card:
        second_name_points += second_card - first_card

    elif first_card == second_card:
        is_number_wars = True
        first_card = int(input())
        second_card = int(input())
        print("Number wars!")

        if first_card > second_card:
            print(f"{first_name} is winner with {first_name_points} points")
        elif second_card > first_card:
            print(f"{second_name} is winner with {second_name_points} points")
        break

    command = input()

if not is_number_wars:
    print(f"{first_name} has {first_name_points} points")
    print(f"{second_name} has {second_name_points} points")
