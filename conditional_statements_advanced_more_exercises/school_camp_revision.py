season = input()
group_type = input()
students_count = int(input())
nights = int(input())

sports_type = ""
price_per_night = 0

if season == "Winter":
    if group_type == "boys":
        price_per_night = 9.60
        sports_type = "Judo"

    elif group_type == "girls":
        price_per_night = 9.60
        sports_type = "Gymnastics"

    elif group_type == "mixed":
        price_per_night = 10
        sports_type = "Ski"

elif season == "Spring":
    if group_type == "boys":
        price_per_night = 7.20
        sports_type = "Tennis"

    elif group_type == "girls":
        price_per_night = 7.20
        sports_type = "Athletics"

    elif group_type == "mixed":
        price_per_night = 9.50
        sports_type = "Cycling"

elif season == "Summer":
    if group_type == "boys":
        price_per_night = 15
        sports_type = "Football"

    elif group_type == "girls":
        price_per_night = 15
        sports_type = "Volleyball"

    elif group_type == "mixed":
        price_per_night = 20
        sports_type = "Swimming"

stay_price = students_count * nights * price_per_night

if students_count >= 50:
    stay_price -= stay_price * 0.5

elif 20 <= students_count < 50:
    stay_price -= stay_price * 0.15

elif 10 <= students_count < 20:
    stay_price -= stay_price * 0.05

print(f"{sports_type} {stay_price:.2f} lv.")
