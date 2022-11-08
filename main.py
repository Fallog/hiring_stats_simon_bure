import sqlite3
import pandas as pd


def extractRows(
    data_frame: pd.DataFrame, last_row: int, first_row: int = 0
) -> pd.DataFrame:
    """Extract the rows of a specified panda dataframe, from first_row to max_row

    Args:
        data_frame (pd.DataFrame): a panda data frame containing the datas
        max_row (int): The index of the last row to be extracted
        first_row (int, optional): The index of the first row to be extracted. Defaults to 0.

    Returns:
        pd.DataFrame: a panda data frame constituted by the extracted rows
    """
    return data_frame.filter(items=list(range(first_row, last_row)), axis="index")


with sqlite3.connect("data/penguins.sqlite") as co:
    penguins_df = pd.read_sql_query("SELECT * FROM penguins", co)
    # print(penguins_df.head())

    # DATA VISUALIZATION
    peng_rows = extractRows(penguins_df, 8, 2)
    print(peng_rows)

    # TRANSFORM IN NUMERIC VALUES
    bill_length = penguins_df.filter(items=["bill_length_mm"], axis="columns")
    print(bill_length)
