deposited_amount = float(input())
deposit_period = int(input())
annual_interest_percentage = float(input())
sum_amount = deposited_amount + deposit_period*(deposited_amount*(annual_interest_percentage/100)/12)

print(sum_amount)
