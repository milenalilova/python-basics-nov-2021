movie_name = input()
salon_type = input()
tickets_count = int(input())

ticket_price = 0

if movie_name == "A Star Is Born":
    if salon_type == "normal":
        ticket_price = 7.50
    elif salon_type == "luxury":
        ticket_price = 10.50
    elif salon_type == "ultra luxury":
        ticket_price = 13.50

elif movie_name == "Bohemian Rhapsody":
    if salon_type == "normal":
        ticket_price = 7.35
    elif salon_type == "luxury":
        ticket_price = 9.45
    elif salon_type == "ultra luxury":
        ticket_price = 12.75

elif movie_name == "Green Book":
    if salon_type == "normal":
        ticket_price = 8.15
    elif salon_type == "luxury":
        ticket_price = 10.25
    elif salon_type == "ultra luxury":
        ticket_price = 13.25

elif movie_name == "The Favourite":
    if salon_type == "normal":
        ticket_price = 8.75
    elif salon_type == "luxury":
        ticket_price = 11.55
    elif salon_type == "ultra luxury":
        ticket_price = 13.95

tickets_sold = tickets_count * ticket_price

print(f"{movie_name} -> {tickets_sold:.2f} lv.")
