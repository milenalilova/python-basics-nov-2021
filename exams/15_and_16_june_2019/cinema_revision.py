salon_capacity = int(input())

command = input()
is_full = False
sales = 0

while command != "Movie time!":
    people = int(command)
    if salon_capacity < people:
        is_full = True
        print("The cinema is full.")
        break
    bill = people * 5
    if people % 3 == 0:
        bill -= 5
    sales += bill
    salon_capacity -= people

    command = input()

if not is_full:
    print(f"There are {salon_capacity} seats left in the cinema.")

print(f"Cinema income - {sales} lv.")
