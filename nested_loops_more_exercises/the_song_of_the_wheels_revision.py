control_num = int(input())
counter = 0
password = ""

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == control_num:
                    if a < b and c > d:
                        print(f'{a}{b}{c}{d}', end=' ')
                        counter += 1
                        if counter == 4:
                            password = f'{a}{b}{c}{d}'
print()
if password:
    print(f"Password: {password}")
else:
    print('No!')
