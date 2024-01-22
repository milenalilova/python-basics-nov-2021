import sys

n = int(input())
first_num = int(input())
second_num = int(input())
previous_sum = first_num + second_num

value = -sys.maxsize
next_sum = 0
diff = 0
condition = True

for i in range(n - 1):
    first_num = int(input())
    second_num = int(input())

    next_sum = first_num + second_num

    if previous_sum != next_sum:
        condition = False
        diff = abs(previous_sum - next_sum)
        if diff > value:
            value = diff

    previous_sum = next_sum

if condition:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={value}")
