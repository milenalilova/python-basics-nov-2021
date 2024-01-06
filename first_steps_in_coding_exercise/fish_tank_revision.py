length_cm = int(input())
height_cm = int(input())
width_cm = int(input())
percentage = float(input())

volume_cm = length_cm * height_cm * width_cm
volume_lit = volume_cm / 1000

litres_needed = volume_lit - volume_lit * (percentage/100)

print(litres_needed)
