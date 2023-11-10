import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file.
    """
    return pd.read_csv(file_path)

def preprocess_data(data):
    """
    Preprocess the data by removing null values and duplicates.
    """
    data = data.dropna()
    data = data.drop_duplicates()
    return data
