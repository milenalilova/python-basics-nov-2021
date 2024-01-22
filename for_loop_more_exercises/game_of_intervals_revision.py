moves = int(input())

result = 0

interval_0_9 = 0
interval_10_19 = 0
interval_20_29 = 0
interval_30_39 = 0
interval_40_50 = 0
invalids = 0

for num in range(moves):
    number = int(input())

    if number < 0 or number > 50:
        result /= 2
        invalids += 1

    elif 0 <= number <= 9:
        result += number * 0.2
        interval_0_9 += 1

    elif 10 <= number <= 19:
        result += number * 0.3
        interval_10_19 += 1

    elif 20 <= number <= 29:
        result += number * 0.4
        interval_20_29 += 1

    elif 30 <= number <= 39:
        result += 50
        interval_30_39 += 1

    elif 40 <= number <= 50:
        result += 100
        interval_40_50 += 1

interval_0_9_percentage = interval_0_9 / moves * 100
interval_10_19_percentage = interval_10_19 / moves * 100
interval_20_29_percentage = interval_20_29 / moves * 100
interval_30_39_percentage = interval_30_39 / moves * 100
interval_40_50_percentage = interval_40_50 / moves * 100
invalids_percentage = invalids / moves * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {interval_0_9_percentage:.2f}%")
print(f"From 10 to 19: {interval_10_19_percentage:.2f}%")
print(f"From 20 to 29: {interval_20_29_percentage:.2f}%")
print(f"From 30 to 39: {interval_30_39_percentage:.2f}%")
print(f"From 40 to 50: {interval_40_50_percentage:.2f}%")
print(f"Invalid numbers: {invalids_percentage:.2f}%")

