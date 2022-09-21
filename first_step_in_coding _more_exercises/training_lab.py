length_in_meters = float(input())
width_in_meters = float(input())

length_in_cm = length_in_meters * 100
width_in_cm = width_in_meters * 100
width_left = width_in_cm - 100
width_desc = width_left // 70
rows = length_in_cm // 120
desc_number = rows * width_desc - 3

print(round(desc_number))
