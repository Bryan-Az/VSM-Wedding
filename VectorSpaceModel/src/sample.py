import pandas as pd

def preprocess_data(data):
    """
    Preprocess the data by removing null values and duplicates.
    """
    data = data.dropna()
    data = data.drop_duplicates()
    return data
