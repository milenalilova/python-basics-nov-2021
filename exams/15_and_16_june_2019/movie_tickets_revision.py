a1 = int(input())
a2 = int(input())
n = int(input())
m = int(n / 2)

for i in range(a1, a2):
    for j in range(1, n):
        for k in range(1, m):
            sum_num = j + k + i
            if i % 2 != 0 and sum_num % 2 != 0:
                print(f"{chr(i)}-{j}{k}{i}")
