number_tabs = int(input())
salary = int(input())

for tabs in range(1, number_tabs + 1):
    web = input()
    if web == "Facebook":
        salary = salary - 150
    elif web == "Instagram":
        salary = salary - 100
    elif web == "Reddit":
        salary = salary - 50
        # if salary <= 0:
        #     break
if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)
