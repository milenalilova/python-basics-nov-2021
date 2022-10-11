width_cake = int(input())
length_cake = int(input())
number_pieces = width_cake * length_cake

while number_pieces > 0:
    command = input()
    if command == "STOP":
        print(f"{number_pieces} pieces are left.")
        break
    pieces_taken = int(command)
    number_pieces -= pieces_taken
    if number_pieces <= 0:
        pieces_left = abs(number_pieces)
        print(f"No more cake left! You need {pieces_left} pieces more.")
