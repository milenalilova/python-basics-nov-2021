a = int(input())
b = int(input())
max_num_passwords = int(input())
counter = 0
condition = False

for aa in range(35, 56):
    for bb in range(64, 97):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                print(f"{(chr(aa))}{chr(bb)}{x}{y}{chr(bb)}{chr(aa)}", end='|')
                counter += 1
                if counter >= max_num_passwords:
                    condition = True
                    break
                elif x >= a and y >= b:
                    condition = True
                else:
                    aa += 1
                    if aa > 55:
                        aa = 35
                    bb += 1
                    if bb > 96:
                        bb = 64

            if condition:
                break
        if condition:
            break
    if condition:
        break

# Variant 2 (better)

# a = int(input())
# b = int(input())
# max_combinations = int(input())
# total_combinations = 0
# symbol_a = 35
# symbol_b = 64
#
# for x in range(1, a + 1):
#     for y in range(1, b + 1):
#         total_combinations += 1
#         if total_combinations > max_combinations:
#             break
#         if symbol_a > 55:
#             symbol_a = 35
#         if symbol_b > 96:
#             symbol_b = 64
#         print(f"{chr(symbol_a)}{chr(symbol_b)}{x}{y}{chr(symbol_b)}{chr(symbol_a)}", end="|")
#         symbol_a += 1
#         symbol_b += 1
