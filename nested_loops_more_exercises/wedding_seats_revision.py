last_sector = input()
rows_sector_first = int(input())
seats_per_odd_row = int(input())
counter = 0
rows_count = rows_sector_first

for sector in range(ord('A'), ord(last_sector) + 1):

    for row in range(1, rows_count + 1):
        if row % 2 == 0:
            seats = seats_per_odd_row + 2
        else:
            seats = seats_per_odd_row

        for seat in range(ord('a'), ord('a') + seats):
            print(f"{chr(sector)}{row}{chr(seat)}")
            counter += 1

    rows_count += 1

print(counter)
