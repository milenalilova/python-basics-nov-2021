from math import floor

book_pages = int(input())
pages_per_hour = int(input())
days_for_reading = int(input())

reading_hours_per_book = book_pages / pages_per_hour
hours_needed_per_day = reading_hours_per_book / days_for_reading

print(floor(hours_needed_per_day))
