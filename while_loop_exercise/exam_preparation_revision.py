negative_notes = int(input())
bad_notes = 0
score = 0
task_count = 0
has_failed = False

task_name = input()
last_task = ""

while task_name != "Enough":
    task_note = int(input())
    last_task = task_name

    if task_note <= 4:
        bad_notes += 1
        if bad_notes >= negative_notes:
            has_failed = True
            break
    score += task_note
    task_count += 1

    task_name = input()

if has_failed:
    print(f"You need a break, {negative_notes} poor grades.")

else:
    average_score = score / task_count

    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {task_count}")
    print(f"Last problem: {last_task}")
