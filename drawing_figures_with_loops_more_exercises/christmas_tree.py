n = int(input())

for i in range(n + 1):
    print(f"{' ' * (n - i)}{'*' * i} | {'*' * i}")


