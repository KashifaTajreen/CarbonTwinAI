import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

def train_model():

    np.random.seed(42)

    n = 1000

    car = np.random.randint(0, 300, n)
    meat = np.random.randint(0, 30, n)
    electricity = np.random.randint(50, 300, n)
    orders = np.random.randint(0, 20, n)

    carbon = (
        car*0.25
        + meat*4
        + electricity*0.8
        + orders*2
        + np.random.normal(0,20,n)
    )

    df = pd.DataFrame({
        "car": car,
        "meat": meat,
        "electricity": electricity,
        "orders": orders,
        "carbon": carbon
    })

    X = df.drop("carbon", axis=1)
    y = df["carbon"]

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    return model