n = int(input())
combinations = 0

for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            if i + j + k == n:
                combinations += 1

print(combinations)
