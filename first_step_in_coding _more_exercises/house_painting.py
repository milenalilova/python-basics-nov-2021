x = float(input())
y = float(input())
h = float(input())
red_paint_use_per_sq_meter = 4.3
green_paint_use_per_sq_meter = 3.4


s_squqre = x * x
s_rectangle = x * y
s_triangle = x * h / 2
s_door = 1.2 * 2
s_window = 1.5 * 1.5
walls_area = 2 * s_squqre + 2 * s_rectangle - s_door - 2 * s_window
roof_area = 2 * s_rectangle + 2 * s_triangle
red_paint_needed = roof_area / red_paint_use_per_sq_meter
green_paint_needed = walls_area / green_paint_use_per_sq_meter

print(f"{green_paint_needed:.2f}")
print(f"{red_paint_needed:.2f}")

