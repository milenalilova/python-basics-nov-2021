country = input()
apparatus = input()

difficulty_points = 0
performance_points = 0
total_points = 0

if apparatus == "ribbon":
    if country == "Russia":
        difficulty_points += 9.100
        performance_points += 9.400
    elif country == "Bulgaria":
        difficulty_points += 9.600
        performance_points += 9.400
    elif country == "Italy":
        difficulty_points += 9.200
        performance_points += 9.500

    # total_points = difficulty_points + performance_points

elif apparatus == "hoop":
    if country == "Russia":
        difficulty_points += 9.300
        performance_points += 9.800
    elif country == "Bulgaria":
        difficulty_points += 9.550
        performance_points += 9.750
    elif country == "Italy":
        difficulty_points += 9.450
        performance_points += 9.350

elif apparatus == "rope":
    if country == "Russia":
        difficulty_points += 9.600
        performance_points += 9.000
    elif country == "Bulgaria":
        difficulty_points += 9.500
        performance_points += 9.400
    elif country == "Italy":
        difficulty_points += 9.700
        performance_points += 9.150

total_points = difficulty_points + performance_points
diff_points = 20 - total_points
diff_percentage = diff_points / 20 * 100

print(f"The team of {country} get {total_points:.3f} on {apparatus}.")
print(f"{diff_percentage:.2f}%")
