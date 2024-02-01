n = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                left_sum = i + j
                right_sum = k + l
                if left_sum == right_sum and n % left_sum == 0:
                    print(f"{i}{j}{k}{l}", end=' ')
