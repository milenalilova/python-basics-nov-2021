n = int(input())
odd_sum = 0
even_sum = 0

for i in range(n):
    num = int(input())

    if i % 2 == 0:
        even_sum += num

    else:
        odd_sum += num

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")

else:
    difference = abs(odd_sum - even_sum)

    print("No")
    print(f"Diff = {difference}")
