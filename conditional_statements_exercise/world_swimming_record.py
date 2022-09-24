record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())

swimming_time = distance_in_meters * time_in_seconds
additional_seconds = distance_in_meters // 15 * 12.5
total_swimming_time = swimming_time + additional_seconds

if total_swimming_time < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {total_swimming_time:.2f} seconds.')

else:
    print(f'No, he failed! He was {(total_swimming_time - record_in_seconds):.2f} seconds slower.')
    