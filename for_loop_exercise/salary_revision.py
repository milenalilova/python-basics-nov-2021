open_tabs_count = int(input())
salary = int(input())

for tab in range(open_tabs_count):
    website = input()

    if website == "Facebook":
        salary -= 150

    elif website == "Instagram":
        salary -= 100

    elif website == "Reddit":
        salary -= 50

if salary <= 0:
    print("You have lost your salary.")

else:
    print(salary)
