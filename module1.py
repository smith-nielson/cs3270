import os
import csv
import pandas as pd
from pathlib import Path
"""
This script grabs a file defined under file_path, 
reads it using pandas and prints first 10 lines and a pandas descirbe 
"""

def load_csv_into_pandas(file_path):
    """
    This function loads a csv file into a pandas dataframe
    :param file_path:
    :return:
    """
    return pd.read_csv(file_path)

def main():
    """
    Main function that defines & returns info on csv file
    :return:
    """
    file_path = "data/weather_test_data.csv"

    try:
        data_frame = load_csv_into_pandas(file_path)
    except FileNotFoundError:
        print(f"File not found {file_path}")
        return

    print("Data frame head")
    print(data_frame.head(10))

    print("Data frame describe")
    print(data_frame.describe())


if __name__ == "__main__":
    main()