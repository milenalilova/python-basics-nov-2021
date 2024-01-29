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
