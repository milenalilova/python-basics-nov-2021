import sys

n = int(input())
max_num = -sys.maxsize
sum_num = 0

for i in range(n):
    num = int(input())
    if num > max_num:
        max_num = num

    sum_num += num

sum_num -= max_num

if sum_num == max_num:
    print("Yes")
    print(f"Sum = {sum_num}")

else:
    difference = abs(sum_num - max_num)
    print("No")
    print(f"Diff = {difference}")
