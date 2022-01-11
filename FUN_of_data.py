import pandas as pd


def readfile(csv_file):
    return pd.read_csv("updated_stock_tickers.csv")

def load_to_df():
    df = readfile("updated_stock_tickers.csv")
print(load_to_df())





