n = int(input())
p_one = 0
p_two = 0
p_three = 0
p_four = 0
p_five = 0

for i in range(n):
    num = int(input())

    if num < 200:
        p_one += 1

    elif 200 <= num <= 399:
        p_two += 1

    elif 400 <= num <= 599:
        p_three += 1

    elif 600 <= num <= 799:
        p_four += 1

    elif num >= 800:
        p_five += 1

p1 = p_one / n * 100
p2 = p_two / n * 100
p3 = p_three / n * 100
p4 = p_four / n * 100
p5 = p_five / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")

