first_num = int(input())
second_num = int(input())

first_num_first_digit = int(str(first_num)[0])
second_num_first_digit = int(str(second_num)[0])
first_num_second_digit = int(str(first_num)[1])
second_num_second_digit = int(str(second_num)[1])
first_num_third_digit = int(str(first_num)[2])
second_num_third_digit = int(str(second_num)[2])
first_num_fourth_digit = int(str(first_num)[3])
second_num_fourth_digit = int(str(second_num)[3])

for i in range(first_num_first_digit, second_num_first_digit + 1):
    for j in range(first_num_second_digit, second_num_second_digit + 1):
        for k in range(first_num_third_digit, second_num_third_digit + 1):
            for l in range(first_num_fourth_digit, second_num_fourth_digit + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    print(f"{i}{j}{k}{l}", end=' ')
