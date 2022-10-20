import pandas as pd

def initial_read(path):
    df = pd.read_csv(path)
    return df.head()
