n = int(input())
double_n = 2 * n
left_sum = 0
right_sum = 0

for i in range(double_n):
    num = int(input())

    if i < n:
        left_sum += num

    elif i >= n:
        right_sum += num

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")

else:
    difference = abs(left_sum - right_sum)
    print(f"No, diff = {difference}")
