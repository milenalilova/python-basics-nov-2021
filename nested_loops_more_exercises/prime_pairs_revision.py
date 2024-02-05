first_initial_value = int(input())
second_initial_value = int(input())
first_diff = int(input())
second_diff = int(input())

first_cap = first_initial_value + first_diff
second_cap = second_initial_value + second_diff

for i in range(first_initial_value, first_cap + 1):
    i_is_not_prime = False
    for m in range(2, i):
        if i % m == 0:
            i_is_not_prime = True
            break

    for j in range(second_initial_value, second_cap + 1):
        j_is_not_prime = False
        for k in range(2, j):
            if j % k == 0:
                j_is_not_prime = True
                break
        if not i_is_not_prime and not j_is_not_prime:
            print(f"{i}{j}", end='')
            print()
