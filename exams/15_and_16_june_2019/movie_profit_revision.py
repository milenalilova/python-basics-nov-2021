film_name = input()
days_count = int(input())
tickets_count = int(input())
tickets_price = float(input())
cinema_percent = int(input())

sales = days_count * tickets_count * tickets_price
profit = sales - sales * cinema_percent / 100

print(f"The profit from the movie {film_name} is {profit:.2f} lv.")
