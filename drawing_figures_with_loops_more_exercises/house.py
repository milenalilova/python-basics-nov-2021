n = int(input())
stars = 0

for i in range((n + 1) // 2):
    if i == 0:
        if n % 2 == 0:
            stars = 2
            print(f"{'-' * ((n - 2) // 2)}{'*' * stars}{'-' * ((n - 2) // 2)}")
        else:
            stars = 1
            print(f"{'-' * ((n - 1) // 2)}{'*' * stars}{'-' * ((n - 1) // 2)}")

    else:

        print(f"{'-' * ((n - stars) // 2)}{'*' * stars}{'-' * ((n - stars) // 2)}")

    stars += 2

for j in range(n // 2):
    print(f"|{(n - 2) * '*'}|")



# Variant 2
# count = int(input())
#
# for i in range((count + 1) // 2):
#     if i == 0:
#         if count % 2 == 0:
#             print(f"{'-' * ((count - 2) // 2)}**{'-' * ((count - 2) // 2)}")
#         else:
#             print(f"{'-' * ((count - 1) // 2)}*{'-' * ((count - 1) // 2)}")
#     else:
#         if count % 2 == 0:
#             print(f"{'-' * ((count - (i+1) * 2) // 2)}{'*' * ((i+ 1) * 2)}{'-' * ((count - (i+1) * 2) // 2)}")
#         else:
#             print(f"{'-' * ((count + 1 - (i+1) * 2) // 2)}{'*' * ((i+ 1) * 2 - 1)}{'-' * ((count + 1 - (i+1) * 2) // 2)}")
#
# for i in range (count - (count + 1) // 2):
#     print(f"|{'*' * (count - 2)}|")