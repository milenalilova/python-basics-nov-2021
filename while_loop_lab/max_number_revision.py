import sys

max_num = -sys.maxsize

command = input()

while command != "Stop":
    num = int(command)
    if num > max_num:
        max_num = num

    command = input()

print(max_num)
