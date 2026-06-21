# simulator.py

def simulate_improvement(current):
    reduced = current * 0.80
    saved = current - reduced

    return round(reduced, 2), round(saved, 2)