# kilometres = int(input())
# time_of_day = input()
#
# taxi_start_tariff = 0.70
# taxi_day_tariff = 0.79
# taxi_night_tariff = 0.90
# bus_tariff = 0.09
# train_tariff = 0.06
# taxi_day_travel_cost = taxi_start_tariff + taxi_day_tariff * kilometres
# taxi_night_travel_cost = taxi_start_tariff + taxi_night_tariff * kilometres
# bus_travel_cost = bus_tariff * kilometres
# train_travel_cost = train_tariff * kilometres
#
# if kilometres < 20:
#     if time_of_day == "day":
#         print(f'{taxi_day_travel_cost:.2f}')
#     elif time_of_day == "night":
#         print(f'{taxi_night_travel_cost:.2f}')
# elif 20 <= kilometres < 100:
#     if time_of_day == "day":
#         if taxi_day_travel_cost <= bus_travel_cost:
#             print(f'{taxi_day_travel_cost:.2f}')
#         else:
#             print(f'{bus_travel_cost:.2f}')
#     elif time_of_day == "night":
#         if taxi_night_travel_cost <= bus_travel_cost:
#             print(f'{taxi_night_travel_cost:.2f}')
#         else:
#             print(f'{bus_travel_cost:.2f}')
# elif kilometres >= 100:
#     if time_of_day == "day":
#         if taxi_day_travel_cost <= bus_travel_cost and taxi_day_travel_cost <= train_travel_cost:
#             print(f'{taxi_day_travel_cost:.2f}')
#         elif bus_travel_cost <= taxi_day_travel_cost and bus_travel_cost <= train_travel_cost:
#             print(f'{bus_travel_cost:.2f}')
#         elif train_travel_cost <= taxi_day_travel_cost and train_travel_cost <= bus_travel_cost:
#             print(f'{train_travel_cost:.2f}')
#     elif time_of_day == "night":
#         if taxi_night_travel_cost <= bus_travel_cost and taxi_night_travel_cost <= train_travel_cost:
#             print(f'{taxi_night_travel_cost:.2f}')
#         elif bus_travel_cost <= taxi_night_travel_cost and bus_travel_cost <= train_travel_cost:
#             print(f'{bus_travel_cost:.2f}')
#         elif train_travel_cost <= taxi_night_travel_cost and train_travel_cost <= bus_travel_cost:
#             print(f'{train_travel_cost:.2f}')


# kilometres = int(input())
# time_of_day = input()
#
# taxi_start_tariff = 0.70
# taxi_day_tariff = 0.79
# taxi_night_tariff = 0.90
# bus_tariff = 0.09
# train_tariff = 0.06
# taxi_day_travel_cost = taxi_start_tariff + taxi_day_tariff * kilometres
# taxi_night_travel_cost = taxi_start_tariff + taxi_night_tariff * kilometres
# bus_travel_cost = bus_tariff * kilometres
# train_travel_cost = train_tariff * kilometres
#
# if kilometres < 20:
#     if time_of_day == "day":
#         print(f'{taxi_day_travel_cost:.2f}')
#     elif time_of_day == "night":
#         print(f'{taxi_night_travel_cost:.2f}')
# elif 20 <= kilometres < 100:
#     if time_of_day == "day":
#         print(f'{min(taxi_day_travel_cost, bus_travel_cost):.2f}')
#     elif time_of_day == "night":
#         print(f'{min(taxi_night_travel_cost, bus_travel_cost):.2f}')
# elif kilometres >= 100:
#     if time_of_day == "day":
#         print(f'{min(taxi_day_travel_cost, bus_travel_cost, train_travel_cost):.2f}')
#     elif time_of_day == "night":
#         print(f'{min(taxi_night_travel_cost, bus_travel_cost, train_travel_cost):.2f}')


kilometres = int(input())
time_of_day = input()

taxi_start_tariff = 0.70
taxi_day_tariff = 0.79
taxi_night_tariff = 0.90
bus_tariff = 0.09
train_tariff = 0.06
taxi_day_travel_cost = taxi_start_tariff + taxi_day_tariff * kilometres
taxi_night_travel_cost = taxi_start_tariff + taxi_night_tariff * kilometres
bus_travel_cost = bus_tariff * kilometres
train_travel_cost = train_tariff * kilometres

if kilometres < 20 and time_of_day == "day":
    print(f'{taxi_day_travel_cost:.2f}')
elif kilometres < 20 and time_of_day == "night":
    print(f'{taxi_night_travel_cost:.2f}')
elif 20 <= kilometres < 100 and time_of_day == "day":
    print(f'{min(taxi_day_travel_cost, bus_travel_cost):.2f}')
elif 20 <= kilometres < 100 and time_of_day == "night":
    print(f'{min(taxi_night_travel_cost, bus_travel_cost):.2f}')
elif kilometres >= 100 and time_of_day == "day":
    print(f'{min(taxi_day_travel_cost, bus_travel_cost, train_travel_cost):.2f}')
elif kilometres >= 100 and time_of_day == "night":
    print(f'{min(taxi_night_travel_cost, bus_travel_cost, train_travel_cost):.2f}')
