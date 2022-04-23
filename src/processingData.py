# (c) Tiago Tamagusko 2022
"""
Add coordinates to the dataset.
"""
from __future__ import annotations

import pandas as pd
from coordinates import coordinates
from coordinates import latitude
from coordinates import longitude


df = pd.read_csv(
    './data/clientAddress.csv',
    sep=';',
    encoding='utf-8',
    index_col=0,
)


def saveData(df, folder='./data/processed/', filename='clientCoordinates.csv', index_col=0):
    """Save a dataframe to a csv file"""
    return df.to_csv(folder + filename, sep=';', encoding='utf-8')


def add_client_coordinates_to_dataset(df):
    """
    Add the coordinates (latitude and longitude) into a dataset based on address.
    Args:
        df: The dataset must have two columns, one for the clients and another for the address.
    """
    df['coordinates'] = df['address'].apply(coordinates).astype(str)
    df['latitude'] = df['address'].apply(latitude).astype(str)
    df['longitude'] = df['address'].apply(longitude).astype(str)
    return df


saveData(add_client_coordinates_to_dataset(df))
