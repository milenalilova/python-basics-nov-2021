x = float(input())
y = float(input())
h = float(input())
door_h = 2
door_w = 1.2
window_side = 1.5
green_paint_coverage_per_sqm = 3.4
red_paint_coverage_per_sqm = 4.3

door_area = door_h * door_w
window_area = window_side ** 2

front_area = x ** 2
back_area = x ** 2
side_area = x * y
roof_front_area = (x * h) / 2
roof_back_area = (x * h) / 2
roof_side_area = x * y

walls_area = front_area - door_area + back_area + side_area - window_area + side_area - window_area
roof_area = roof_front_area + roof_back_area + 2 * roof_side_area

green_paint_quantity = walls_area / green_paint_coverage_per_sqm
red_paint_quantity = roof_area / red_paint_coverage_per_sqm

print(f"{green_paint_quantity:.2f}")
print(f"{red_paint_quantity:.2f}")
