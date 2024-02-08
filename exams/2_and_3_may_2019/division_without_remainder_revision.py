n = int(input())

div_2 = 0
div_3 = 0
div_4 = 0

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        div_2 += 1

    if num % 3 == 0:
        div_3 += 1

    if num % 4 == 0:
        div_4 += 1

percentage_div_2 = div_2 / n * 100
percentage_div_3 = div_3 / n * 100
percentage_div_4 = div_4 / n * 100

print(f"{percentage_div_2:.2f}%")
print(f"{percentage_div_3:.2f}%")
print(f"{percentage_div_4:.2f}%")
