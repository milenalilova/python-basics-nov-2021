change = float(input())
counter = 0

while change > 0:
    if change >= 2:
        change -= 2

    elif change >= 1:
        change -= 1

    elif change >= 0.5:
        change -= 0.5

    elif change >= 0.2:
        change -= 0.2

    elif change >= 0.1:
        change -= 0.1

    elif change >= 0.05:
        change -= 0.05

    elif change >= 0.02:
        change -= 0.02

    elif change >= 0.01:
        change -= 0.01

    change = round(change, 2)
    counter += 1

print(counter)
