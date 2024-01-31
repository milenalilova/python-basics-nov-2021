trainers_count = int(input())
total_notes = 0
count = 0

command = input()

while command != "Finish":
    sum_notes = 0
    av_note = 0
    for trainer in range(trainers_count):
        note = float(input())
        count += 1
        total_notes += note
        sum_notes += note
        av_note = sum_notes / trainers_count
    print(f"{command} - {av_note:.2f}.")

    command = input()

final_assessment = total_notes / count

print(f"Student's final assessment is {final_assessment:.2f}.")
