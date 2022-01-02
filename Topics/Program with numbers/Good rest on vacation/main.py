# put your python code here
duration_in_days = int(input())
daily_food_cost = int(input())
flight_cost = int(input())
night_cost = int(input())
total_food_cost = duration_in_days * daily_food_cost
total_hotel_cost = (duration_in_days - 1) * night_cost
total_flight_cost = 2 * flight_cost
print(total_food_cost + total_hotel_cost + total_flight_cost)