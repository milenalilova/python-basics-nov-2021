book_name = input()
text = input()
counter = 0
is_found = False

while text != "No More Books":

    if text == book_name:
        is_found = True
        break

    counter += 1

    text = input()

if is_found:
    print(f"You checked {counter} books and found it.")

else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
