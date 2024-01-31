command = input()
prime_sum = 0
non_prime_sum = 0

while command != "stop":
    is_not_prime = False
    num = int(command)

    if num < 0:
        print("Number is negative.")

    else:
        for i in range(2, num):
            if num % i == 0:
                is_not_prime = True
                break

    if is_not_prime and num >= 0:
        non_prime_sum += num
    elif not is_not_prime and num>=0:
        prime_sum += num

    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
