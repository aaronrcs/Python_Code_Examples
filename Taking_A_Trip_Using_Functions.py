# Function to get the cost of the hotel
def hotel_cost(nights):
    return 140 * nights

# Function to get the cost of the plane ride
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

# Function to get the cost of the rental car
def rental_car_cost(days):
    price_of_car = days * 40

    if days >= 7:
        price_of_car -= 50
    elif days >= 3:
        price_of_car -= 20

    return price_of_car


# Function to get the total costs of vacation expenses
def trip_cost(city, days, spending_money):
    return "The rental cost was $%s, the total hotel cost was $%d, the plane ride cost was $%d and money spend $%d" \
           % (rental_car_cost(days), + hotel_cost(days), + plane_ride_cost(city), + spending_money)

print ("This is my total expenses for Los Angeles: ")
print (trip_cost("Los Angeles", 5, 600))