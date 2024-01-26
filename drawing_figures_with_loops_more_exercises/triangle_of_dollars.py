# n = int(input())
#
# for i in range(1, n+1):
#     print(i * "$ ")
#


n = int(input())

for row in range(n):
    print('$', end='')
    for col in range(row):
        print(' $', end='')
    print()

