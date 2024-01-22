stadium_capacity = int(input())
fans_count = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for fan in range(1, fans_count + 1):
    sector = input()

    if sector == "A":
        sector_a += 1

    elif sector == "B":
        sector_b += 1

    elif sector == "V":
        sector_v += 1

    elif sector == "G":
        sector_g += 1

sector_a_percentage = sector_a / fans_count * 100
sector_b_percentage = sector_b / fans_count * 100
sector_v_percentage = sector_v / fans_count * 100
sector_g_percentage = sector_g / fans_count * 100
fans_percentage = fans_count / stadium_capacity * 100

print(f"{sector_a_percentage:.2f}%")
print(f"{sector_b_percentage:.2f}%")
print(f"{sector_v_percentage:.2f}%")
print(f"{sector_g_percentage:.2f}%")
print(f"{fans_percentage:.2f}%")
