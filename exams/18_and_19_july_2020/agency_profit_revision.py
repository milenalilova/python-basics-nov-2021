aircraft_name = input()
adults_tickets_count = int(input())
kids_tickets_count = int(input())
adults_price = float(input())
service_charge = float(input())

total_tickets_sold = adults_tickets_count + kids_tickets_count
kids_price = adults_price - adults_price * 0.70
sales = adults_tickets_count * adults_price + kids_tickets_count * kids_price + total_tickets_sold * service_charge

profit = sales * 0.20

print(f"The profit of your agency from {aircraft_name} tickets is {profit:.2f} lv.")
