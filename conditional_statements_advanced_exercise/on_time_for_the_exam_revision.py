starting_hour = int(input())
starting_minute = int(input())
arriving_hour = int(input())
arriving_minute = int(input())

starting_time = starting_hour * 60 + starting_minute
arriving_time = arriving_hour * 60 + arriving_minute

difference_minutes = starting_time - arriving_time

if difference_minutes < 0:
    print("Late")
    difference_minutes = abs(difference_minutes)

    if difference_minutes <= 59:
        print(f"{difference_minutes} minutes after the start")
    else:
        difference_hours = difference_minutes // 60
        difference_minutes = difference_minutes % 60
        if difference_minutes < 10:
            print(f"{difference_hours}:0{difference_minutes} hours after the start")
        else:
            print(f"{difference_hours}:{difference_minutes} hours after the start")

elif difference_minutes == 0:
    print("On time")

elif 0 < difference_minutes <= 30:
    print("On time")
    if difference_minutes <= 59:
        print(f"{difference_minutes} minutes before the start")
    else:
        difference_hours = difference_minutes // 60
        difference_minutes = difference_minutes % 60
        if difference_minutes < 10:
            print(f"{difference_hours}:0{difference_minutes} hours before the start")
        else:
            print(f"{difference_hours}:{difference_minutes} hours before the start")

elif difference_minutes > 30:
    print("Early")
    if difference_minutes <= 59:
        print(f"{difference_minutes} minutes before the start")
    else:
        difference_hours = difference_minutes // 60
        difference_minutes = difference_minutes % 60
        if difference_minutes < 10:
            print(f"{difference_hours}:0{difference_minutes} hours before the start")
        else:
            print(f"{difference_hours}:{difference_minutes} hours before the start")
