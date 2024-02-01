first_cap = int(input())
second_cap = int(input())
third_cap = int(input())

for i in range(1, first_cap + 1):
    for j in range(2, second_cap + 1):
        for k in range(1, third_cap + 1):
            if i % 2 == 0 and (j == 2 or j == 3 or j == 5 or j == 7) and k % 2 == 0:
                print(i, j, k)
