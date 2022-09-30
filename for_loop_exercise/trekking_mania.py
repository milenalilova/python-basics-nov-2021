groups_count = int(input())
musala_climbers_count = 0
monblan_climbers_count = 0
kilimanjaro_climbers_count = 0
k2_climbers_count = 0
everest_climbers_count = 0
total_climbers_count = 0

for group in range(groups_count):
    people_count = int(input())
    total_climbers_count += people_count
    if people_count <= 5:
        musala_climbers_count += people_count
    elif people_count <= 12:
        monblan_climbers_count += people_count
    elif people_count <= 25:
        kilimanjaro_climbers_count += people_count
    elif people_count <= 40:
        k2_climbers_count += people_count
    elif people_count >= 41:
        everest_climbers_count += people_count
print(f"{musala_climbers_count / total_climbers_count * 100:.2f}%")
print(f"{monblan_climbers_count / total_climbers_count * 100:.2f}%")
print(f"{kilimanjaro_climbers_count / total_climbers_count * 100:.2f}%")
print(f"{k2_climbers_count / total_climbers_count * 100:.2f}%")
print(f"{everest_climbers_count / total_climbers_count * 100:.2f}%")
