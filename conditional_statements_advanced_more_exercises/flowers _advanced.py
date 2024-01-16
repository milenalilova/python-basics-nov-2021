chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_holiday = input()

flowers_count = chrysanthemums_count + roses_count + tulips_count
chrysanthemum_price = 0
rose_price = 0
tulip_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    rose_price = 4.1
    tulip_price = 2.5

elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    rose_price = 4.5
    tulip_price = 4.15

if is_holiday == "Y":
    chrysanthemum_price += chrysanthemum_price * 0.15
    rose_price += rose_price * 0.15
    tulip_price += tulip_price * 0.15

bouquet_price = chrysanthemums_count * chrysanthemum_price + roses_count * rose_price + tulips_count * tulip_price

if tulips_count > 7 and season == "Spring":
    bouquet_price -= bouquet_price * 0.05

if roses_count >= 10 and season == "Winter":
    bouquet_price -= bouquet_price * 0.1

if flowers_count > 20:
    bouquet_price -= bouquet_price * 0.2

bouquet_price += 2

print(f"{bouquet_price:.2f}")
