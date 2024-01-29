n = int(input())

for i in range(n):
    if i == 0 or i == n - 1:
        print(f'{2 * n * "*"}{n * " "}{2 * n * "*"}')
    elif i == (n - 1) // 2:
        print(f'*{"/" * (n * 2 - 2)}*{n * "|"}*{(n * 2 - 2) * "/"}*')
    else:
        print(f'*{"/" * (n * 2 - 2)}*{n * " "}*{(n * 2 - 2) * "/"}*')


# Variant 2

# count = int(input())

# print(f"{'*' * (count * 2)}{' ' * count}{'*' * (count * 2)}")

# for i in range(count - 2):
#     if i == (count - 1) // 2 - 1:
#         print(f"*{'/' * (count * 2 - 2)}*{'|' * count}*{'/' * (count * 2 - 2)}*")
#     else:
#         print(f"*{'/' * (count * 2 - 2)}*{' ' * count}*{'/' * (count * 2 - 2)}*")

# print(f"{'*' * (count * 2)}{' ' * count}{'*' * (count * 2)}")

