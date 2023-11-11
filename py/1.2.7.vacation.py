def hotel_cost(nights):
    nights *= 140
    return nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return plane_ride_cost(city)
    elif city == "Tampa":
        return plane_ride_cost(city)
    elif city == "Pittsburgh":
        return plane_ride_cost(city)
    elif city == "Los Angeles":
        return plane_ride_cost(city)

def rental_car_cost(days):
    if days >= 7:
        days *= 40 (-50)
        return rental_car_cost(days)
    elif days >= 3:
        days *= 40 (-30)
        return rental_car_cost(days)
    else:
        days == 40
        return rental_car_cost(days)

def trip_cost(city, days, spending_money):
    ''' Find the sums of rental, hotel, plane cost '''
    ''' hotel == rental car '''
    
    return rental_car_cost(days)
    return hotel_cost(days)
    return plane_ride_cost(city)
    # print trip_cost("SOME CITY", NUM_DAYS, SPENDING_MONEY)
    print trip_cost("Los Angeles", 5, 600)