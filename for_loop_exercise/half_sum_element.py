import sys

n = int(input())
sum_numbers = 0
max_number = -sys.maxsize

for numbers in range(0, n):
    num = int(input())
    if num > max_number:
        max_number = num
    sum_numbers = sum_numbers + num
if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(max_number - (sum_numbers - max_number))}")
