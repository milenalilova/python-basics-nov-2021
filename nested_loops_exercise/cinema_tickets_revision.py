movie_name = input()
total_tickets = 0
students_tickets = 0
standard_tickets = 0
kids_tickets = 0

while movie_name != "Finish":
    free_seats = int(input())
    command = input()
    occupied_seats = 0
    # students_tickets = 0
    # standard_tickets = 0
    # kids_tickets = 0

    while command != "End":
        if command == "student":
            students_tickets += 1
        elif command == "standard":
            standard_tickets += 1
        elif command == "kid":
            kids_tickets += 1
        occupied_seats += 1
        total_tickets += 1

        if occupied_seats >= free_seats:
            break

        command = input()
    occupation_percentage = occupied_seats * 100 / free_seats
    print(f"{movie_name} - {occupation_percentage:.2f}% full.")

    movie_name = input()

print(f"Total tickets: {total_tickets}")
print(f"{(students_tickets * 100 / total_tickets):.2f}% student tickets.")
print(f"{(standard_tickets * 100 / total_tickets):.2f}% standard tickets.")
print(f"{(kids_tickets * 100 / total_tickets):.2f}% kids tickets.")
