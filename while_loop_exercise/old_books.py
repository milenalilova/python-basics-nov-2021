book_name = input()
book_counter = 0

searched_book = input()

while searched_book != book_name:
    if searched_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_counter} books.")
        break
    book_counter += 1
    searched_book = input()
if searched_book == book_name:
    print(f"You checked {book_counter} books and found it.")

# book_name = input()
# book_counter = 0
#
# is_book_found = False
#
# current_book = input()
#
# while current_book != "No More Books":
#     if current_book == book_name:
#         is_book_found = True
#         print(f"You checked {book_counter} books and found it.")
#         break
#     book_counter += 1
#     current_book = input()
# if not is_book_found:
#     print("The book you search is not here!")
#     print(f"You checked {book_counter} books.")
