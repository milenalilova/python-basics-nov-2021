n = int(input())

for i in range(n):
    if i == 0 or i == n - 1:
        figure = (n-2)*" -"
        print(f"+{figure} +")
    else:
        figure = (n - 2) * " -"
        print(f"|{figure} |")
