import sys

films_count = int(input())

highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
highest_rating_film = ''
lowest_rating_film = ''
total_rating = 0

for film in range(films_count):
    film_name = input()
    film_rating = float(input())

    if film_rating > highest_rating:
        highest_rating = film_rating
        highest_rating_film = film_name
    elif film_rating<lowest_rating:
        lowest_rating = film_rating
        lowest_rating_film = film_name

    total_rating += film_rating

average_rating = total_rating / films_count

print(f"{highest_rating_film} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rating_film} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
