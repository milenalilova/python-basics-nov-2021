name = input()
win_points = 0
winner_name = ''
second_win_points = 0
second_winner_name = ''

while name != "Stop":
    points = 0

    for ch in range(len(name)):
        num = int(input())
        if num == ord(name[ch]):
            points += 10
        else:
            points += 2

        if points > win_points:
            win_points = points
            winner_name = name
        elif points == win_points:
            second_win_points = points
            second_winner_name = name

    name = input()

if win_points > second_win_points:
    print(f"The winner is {winner_name} with {win_points} points!")
elif win_points == second_win_points:
    print(f"The winner is {second_winner_name} with {second_win_points} points!")

