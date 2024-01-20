groups_count = int(input())
total_people_count = 0
musala_count = 0
montblanc_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

for group in range(groups_count):
    group_members = int(input())

    if group_members <= 5:
        musala_count += group_members

    elif 6 <= group_members <= 12:
        montblanc_count += group_members

    elif 13 <= group_members <= 25:
        kilimanjaro_count += group_members

    elif 26 <= group_members <= 40:
        k2_count += group_members

    elif group_members >= 41:
        everest_count += group_members

    total_people_count += group_members

musala_percentage = musala_count / total_people_count * 100
montblanc_percentage = montblanc_count / total_people_count * 100
kilimanjaro_percentage = kilimanjaro_count / total_people_count * 100
k2_percentage = k2_count / total_people_count * 100
everest_percentage = everest_count / total_people_count * 100

print(f"{musala_percentage:.2f}%")
print(f"{montblanc_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")
