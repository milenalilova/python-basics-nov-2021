deposited_sum = float(input())
deposit_period = int(input())
interest = float(input())
final_sum = deposited_sum + deposit_period * ((deposited_sum * (interest/100)) / 12)

print(final_sum)
