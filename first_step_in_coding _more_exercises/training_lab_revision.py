width = float(input())
height = float(input())
seat_width = 120
seat_height = 70

width_cm = width * 100
height_cm = height * 100

rows = width_cm // seat_width
sits_per_row = (height_cm - 100) // seat_height
desc_number = rows * sits_per_row - 3

print(round(desc_number))
