budget = float(input())
videocards = float(input())
processors = float(input())
rams = float(input())

videocard_price = 250
processor_price = videocards * videocard_price * 0.35
rams_price = videocards * videocard_price * 0.1

order_cost = videocards * videocard_price + processors * processor_price + rams * rams_price

if videocards > processors:
    order_cost = order_cost - order_cost * 0.15

difference = budget - order_cost

if budget >= order_cost:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(difference):.2f} leva more!")
