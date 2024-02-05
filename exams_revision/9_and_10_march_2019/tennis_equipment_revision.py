from math import floor, ceil

racket_price = float(input())
racket_count = int(input())
shoes_count = int(input())

shoes_price = racket_price / 6

equipment_price = racket_count * racket_price + shoes_count * shoes_price
equipment_price += equipment_price / 5

print(f"Price to be paid by Djokovic {floor(equipment_price / 8)}")
print(f"Price to be paid by sponsors {ceil(equipment_price / 8 * 7)}")
