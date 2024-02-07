film_name = input()

total_tickets_sold = 0
student_seats_sold = 0
standard_seats_sold = 0
kid_seats_sold = 0

while film_name != "Finish":
    free_seats = int(input())
    command = input()
    seats_sold = 0

    while command != "End":
        if command == "student":
            student_seats_sold += 1
        elif command == "standard":
            standard_seats_sold += 1
        elif command == "kid":
            kid_seats_sold += 1

        seats_sold += 1
        total_tickets_sold += 1
        if seats_sold == free_seats:
            break

        command = input()

    seats_sold_percentage = seats_sold / free_seats * 100
    print(f"{film_name} - {seats_sold_percentage:.2f}% full.")

    film_name = input()

student_seats_percentage = student_seats_sold / total_tickets_sold * 100
standard_seats_percentage = standard_seats_sold / total_tickets_sold * 100
kid_seats_percentage = kid_seats_sold / total_tickets_sold * 100

print(f"Total tickets: {total_tickets_sold}")
print(f"{student_seats_percentage:.2f}% student tickets.")
print(f"{standard_seats_percentage:.2f}% standard tickets.")
print(f"{kid_seats_percentage:.2f}% kids tickets.")
