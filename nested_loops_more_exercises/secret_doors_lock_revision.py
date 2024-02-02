hundreds_cap = int(input())
tens_cap = int(input())
units_cap = int(input())

for i in range(1, hundreds_cap + 1):
    for j in range(1, tens_cap + 1):
        for k in range(1, units_cap + 1):
            if i % 2 == 0 and k % 2 == 0 and (j == 2 or j == 3 or j == 5 or j == 7):
                print(i, j, k)
