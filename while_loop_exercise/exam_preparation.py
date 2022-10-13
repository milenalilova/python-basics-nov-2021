failed_threshold = int(input())
problems_solved = 0
failed_times = 0
grades_sum = 0
last_problem = ""
has_failed = True

while failed_times < failed_threshold:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    problems_solved += 1
    last_problem = problem_name
if not has_failed:
    print(f"Average score: {grades_sum / problems_solved:.2f}")
    print(f"Number of problems: {problems_solved}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {failed_times} poor grades.")
