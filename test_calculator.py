from calculator import calculate_carbon

def test_calculate_carbon():
    data = {
        "car_km": 100,
        "bike_km": 0,
        "bus_km": 0,
        "metro_km": 0,
        "meat_meals": 5,
        "veg_meals": 10,
        "electricity_units": 100,
        "ac_hours": 2,
        "clothes": 1,
        "online_orders": 2,
        "plastic_items": 5
    }

    result = calculate_carbon(data)

    assert result > 0