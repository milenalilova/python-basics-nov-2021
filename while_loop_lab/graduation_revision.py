name = input()
grade = 1
counter = 0
sum_grades = 0
condition = False

while grade <= 12:
    note = float(input())

    if note >= 4:
        sum_grades += note
        grade += 1
        counter = 0
    else:
        counter += 1
        if counter >= 2:
            condition = True
            break

if condition:
    print(f"{name} has been excluded at {grade} grade")

else:
    average_grade = sum_grades / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
