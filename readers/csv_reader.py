import pandas as pd


def read_csv(path):
    df = pd.read_csv(path, header=None)
    df.insert(0, "id", range(1, len(df) + 1))
    df.insert(5, "id", range(1, len(df) + 1), allow_duplicates=True)
    return df
