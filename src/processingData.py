# (c) Tiago Tamagusko 2022
"""
Add coordinates to the dataset.
"""
from __future__ import annotations

import pandas as pd
from coordinates import coordinates


df = pd.read_csv(
    './data/clientAddress.csv', sep=';',
    encoding='utf-8', index_col=0,
)


def saveData(df, folder='./data/processed/', filename='clientAddressCoordinates.csv', index_col=0):
    """Save a dataframe to a csv file"""
    return df.to_csv(folder + filename, sep=';', encoding='utf-8')


def add_client_coordinates_to_dataset(df):
    """
    Returns the coordinates of a client list.
    Args:
        dataset: The dataset must have two columns, one for the clients and one for the address.
    """
    df['coordinates'] = df['address'].apply(coordinates)
    return df


saveData(add_client_coordinates_to_dataset(df))
