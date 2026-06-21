import pandas as pd

def load_data():
    return pd.read_csv(
        "data/galactic_civilization_dataset.csv"
    )