from math import ceil

easter_breads_count = int(input())

sugar_kg = 0
flour_kg = 0
max_sugar = 0
max_flour = 0

for easter_breads in range(easter_breads_count):
    sugar_gr = int(input())
    flour_gr = int(input())

    if sugar_gr > max_sugar:
        max_sugar = sugar_gr
    if flour_gr > max_flour:
        max_flour = flour_gr

    sugar_kg += sugar_gr
    flour_kg += flour_gr

sugar_packs = ceil(sugar_kg / 950)
flour_packs = ceil(flour_kg / 750)

print(f"Sugar: {sugar_packs}")
print(f"Flour: {flour_packs}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
