number = int(input())

valid = 100 <= number <= 200 or number == 0
if not valid:
    print("invalid")

# variant 2

# number = int(input())
#
# is_valid = False
# if 100 <= number <= 200 or number == 0:
#     is_valid = True
# if not is_valid:
#     print("invalid")
