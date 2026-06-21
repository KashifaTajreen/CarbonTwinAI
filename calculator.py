# calculator.py

def calculate_carbon(data):
    carbon = 0

    # Transport
    carbon += data["car_km"] * 0.21
    carbon += data["bike_km"] * 0.10
    carbon += data["bus_km"] * 0.08
    carbon += data["metro_km"] * 0.04

    # Food
    carbon += data["meat_meals"] * 5
    carbon += data["veg_meals"] * 1.5

    # Energy
    carbon += data["electricity_units"] * 0.82
    carbon += data["ac_hours"] * 0.5

    # Shopping
    carbon += data["clothes"] * 8
    carbon += data["online_orders"] * 2

    # Waste
    carbon += data["plastic_items"] * 0.1

    return round(carbon, 2)