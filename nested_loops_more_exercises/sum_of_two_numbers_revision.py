start_num = int(input())
end_num = int(input())
magic_num = int(input())

combination_num = 0
first_num = 0
second_num = 0

is_found = False

for i in range(start_num, end_num + 1):
    for j in range(start_num, end_num + 1):
        combination_num += 1
        if i + j == magic_num:
            is_found = True
            first_num = i
            second_num = j
            break
    if is_found:
        break

if is_found:
    print(f"Combination N:{combination_num} ({first_num} + {second_num} = {magic_num})")
else:
    print(f"{combination_num} combinations - neither equals {magic_num}")
