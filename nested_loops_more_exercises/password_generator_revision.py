n = int(input())
l = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(l):
            for x in range(l):
                for y in range(1, n + 1):
                    if y > i and y > j:
                        print(f"{i}{j}{chr(97 + k)}{chr(97 + x)}{y}", end=' ')
