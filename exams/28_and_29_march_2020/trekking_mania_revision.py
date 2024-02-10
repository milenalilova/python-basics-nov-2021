groups_count = int(input())
musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_people = 0

for group in range(groups_count):
    people_count = int(input())
    total_people += people_count

    if people_count <= 5:
        musala += people_count

    elif 6 <= people_count <= 12:
        montblanc += people_count

    elif 13 <= people_count <= 25:
        kilimanjaro += people_count

    elif 26 <= people_count <= 40:
        k2 += people_count

    elif people_count >= 41:
        everest += people_count

musala_percentage = musala / total_people * 100
montblanc_percentage = montblanc / total_people * 100
kilimanjaro_percentage = kilimanjaro / total_people * 100
k2_percentage = k2 / total_people * 100
everest_percentage = everest / total_people * 100

print(f"{musala_percentage:.2f}%")
print(f"{montblanc_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")
