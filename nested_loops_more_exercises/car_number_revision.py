first_num = int(input())
second_num = int(input())

for i in range(first_num, second_num + 1):
    for j in range(first_num, second_num + 1):
        for k in range(first_num, second_num + 1):
            for l in range(first_num, second_num + 1):
                sum_nums = j + k
                if i % 2 == 0 and l % 2 != 0 and i > l and sum_nums % 2 == 0:
                    print(f"{i}{j}{k}{l}", end=' ')

                elif i % 2 != 0 and l % 2 == 0 and i > l and sum_nums % 2 == 0:
                    print(f"{i}{j}{k}{l}", end=' ')
