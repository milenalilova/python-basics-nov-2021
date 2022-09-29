number_of_inputs = int(input())
left_sum = 0
right_sum = 0

for numbers in range(2 * number_of_inputs):
    current_number = int(input())
    if numbers < number_of_inputs:
        left_sum = left_sum + current_number
    else:
        right_sum = right_sum + current_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
