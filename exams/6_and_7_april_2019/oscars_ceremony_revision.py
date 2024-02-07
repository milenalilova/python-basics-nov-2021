rent = int(input())

statue_cost = rent - rent * 0.3
catering_cost = statue_cost - statue_cost * 0.15
sound_cost = catering_cost / 2

total_cost = rent + statue_cost + catering_cost + sound_cost

print(f"{total_cost:.2f}")
