first_letter = input()
second_letter = input()
except_letter = input()
counter = 0

for i in range(ord(first_letter), ord(second_letter) + 1):
    for j in range(ord(first_letter), ord(second_letter) + 1):
        for k in range(ord(first_letter), ord(second_letter) + 1):
            if chr(i) != except_letter and chr(j) != except_letter and chr(k) != except_letter:
                counter += 1
                print(f"{chr(i)}{chr(j)}{chr(k)}", end=' ')

print(counter)
