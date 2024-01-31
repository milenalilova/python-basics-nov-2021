number = int(input())

for num in range(1111, 10000):
    num_to_str = str(num)
    condition = True
    for ch in range(len(num_to_str)):
        digit = int(num_to_str[ch])
        if digit == 0:
            condition = False
        elif number % digit != 0:
            condition = False
    if condition:
        print(num, end=' ')
