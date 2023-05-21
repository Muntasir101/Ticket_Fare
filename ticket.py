def calculate_flight_cost(distance, departure_date, service_class):
    if distance < 500:
        cost = 100
    elif 500 <= distance <= 1000:
        if departure_date <= 7:
            cost = distance * 0.10
        elif departure_date <= 30:
            cost = distance * 0.08
        elif departure_date <= 90:
            cost = distance * 0.06
        else:
            cost = 0  # Invalid departure date
    elif distance > 1000:
        if departure_date <= 7:
            cost = distance * 0.30
        elif departure_date <= 30:
            cost = distance * 0.25
        elif departure_date <= 90:
            cost = distance * 0.20
        else:
            cost = 0  # Invalid departure date
    else:
        cost = 0  # Invalid distance

    if service_class == 'Business':
        cost *= 2
    elif service_class == 'First':
        cost *= 3

    return cost

# Example usage:
distance = 70 # Distance in miles
departure_date = 15  # Departure date in days
service_class = 'First'  # Service class

flight_cost = calculate_flight_cost(distance, departure_date, service_class)
print("Flight cost: $", flight_cost)
