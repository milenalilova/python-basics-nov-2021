import sys

min_num = sys.maxsize

command = input()

while command != "Stop":
    num = int(command)
    if num < min_num:
        min_num = num

    command = input()

print(min_num)
