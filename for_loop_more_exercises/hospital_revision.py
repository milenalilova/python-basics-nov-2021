hospital_period = int(input())
treated_patients = 0
untreated_patients = 0
doctors = 7

for day in range(1, hospital_period + 1):
    waiting_patients = int(input())
    if day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if waiting_patients <= doctors:
        treated_patients += waiting_patients

    else:
        treated_patients += doctors
        untreated_patients += waiting_patients - doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
