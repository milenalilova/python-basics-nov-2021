first_num = int(input())
second_num = int(input())
magic_num = int(input())
counter = 0
first_combination = 0
left_num = 0
right_num = 0
condition = False

for i in range(first_num, second_num + 1):
    for j in range(first_num, second_num + 1):
        result = i + j
        counter += 1
        if result == magic_num:
            if condition:
                continue
            left_num = i
            right_num = j
            first_combination = counter
            condition = True

if condition:
    print(f"Combination N:{first_combination} ({left_num} + {right_num} = {magic_num})")
else:
    print(f"{counter} combinations - neither equals {magic_num}")
