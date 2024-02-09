count = 0
best_rating = 0
best_movie = ''

while count <= 7:
    movie_name = input()
    if movie_name == "STOP":
        break
    rating = 0

    for ch in range(len(movie_name)):
        rating += (ord(movie_name[ch]))
        if movie_name[ch].islower():
            rating -= 2 * len(movie_name)
        elif movie_name[ch].isupper():
            rating -= len(movie_name)
    if rating > best_rating:
        best_rating = rating
        best_movie = movie_name

    count += 1
    if count>=7:
        print("The limit is reached.")
        break

print(f"The best movie for you is {best_movie} with {best_rating} ASCII sum.")
