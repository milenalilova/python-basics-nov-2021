juniors_count = int(input())
seniors_count = int(input())
terrain_type = input()

if terrain_type == "trail":
    juniors_fee = 5.5
    seniors_fee = 7
elif terrain_type == "cross-country":
    juniors_fee = 8
    seniors_fee = 9.5
    if juniors_count + seniors_count >= 50:
        juniors_fee -= juniors_fee * 0.25
        seniors_fee -= seniors_fee * 0.25
elif terrain_type == "downhill":
    juniors_fee = 12.25
    seniors_fee = 13.75
elif terrain_type == "road":
    juniors_fee = 20
    seniors_fee = 21.5
    total_fees = juniors_count * juniors_fee + seniors_count * seniors_fee
