import pandas as pd

def load_data():
    return pd.DataFrame({
        "x": range(10),
        "y": [v**2 for v in range(10)]
    })
