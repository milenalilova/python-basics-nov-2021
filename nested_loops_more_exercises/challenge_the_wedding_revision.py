men_count = int(input())
women_count = int(input())
max_table_count = int(input())
counter = 0

for man in range(1, men_count + 1):
    for woman in range(1, women_count + 1):
        counter += 1
        if counter / 2 >= max_table_count:
            break
        counter += 1
        print(f"({man} <-> {woman})", end=' ')
