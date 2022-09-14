number_pages_per_book = int(input())
number_pages_per_hour = int(input())
days_needed_to_reed_book = int(input())
reading_hours_needed_per_day = (number_pages_per_book/number_pages_per_hour)/days_needed_to_reed_book

print(round(reading_hours_needed_per_day))
