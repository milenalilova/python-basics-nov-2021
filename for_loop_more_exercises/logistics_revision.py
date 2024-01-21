cargo_counts = int(input())

minibus_tons = 0
truck_tons = 0
train_tons = 0

total_weight = 0
total_price = 0

for cargo in range(cargo_counts):
    cargo_tons = int(input())
    total_weight += cargo_tons

    if cargo_tons <= 3:
        minibus_tons += cargo_tons
        total_price += cargo_tons * 200

    elif 4 <= cargo_tons <= 11:
        truck_tons += cargo_tons
        total_price += cargo_tons * 175

    elif cargo_tons >= 12:
        train_tons += cargo_tons
        total_price += cargo_tons * 120

average_price = total_price / total_weight
minibus_tons_percent = minibus_tons / total_weight * 100
truck_tons_percent = truck_tons / total_weight * 100
train_tons_percent = train_tons / total_weight * 100

print(f"{average_price:.2f}")
print(f"{minibus_tons_percent:.2f}%")
print(f"{truck_tons_percent:.2f}%")
print(f"{train_tons_percent:.2f}%")
