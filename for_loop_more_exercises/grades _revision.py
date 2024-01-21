students_count = int(input())
notes_value = 0

failed = 0
median = 0
good = 0
top = 0

for student in range(1, students_count + 1):
    grade = float(input())
    notes_value += grade

    if 2 <= grade <= 2.99:
        failed += 1

    elif 3 <= grade <= 3.99:
        median += 1

    elif 4 <= grade <= 4.99:
        good += 1

    elif grade >= 5:
        top += 1

top_grades_percentage = top / students_count * 100
good_grades_percentage = good / students_count * 100
median_grades_percentage = median / students_count * 100
failed_grades_percentage = failed / students_count * 100

average_grade = notes_value / students_count

print(f"Top students: {top_grades_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {good_grades_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {median_grades_percentage:.2f}%")
print(f"Fail: {failed_grades_percentage:.2f}%")
print(f"Average: {average_grade:.2f}")
