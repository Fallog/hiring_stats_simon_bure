import sqlite3
import pandas as pd
from descritpion import freq_table
from descritpion import histogram


def getNbRows(data_frame: pd.DataFrame) -> int:
    """Returns the total number of rows of a panda data frame.

    Args:
        data_frame (pd.DataFrame): a panda data frame

    Returns:
        int: index of the last row of data_frame
    """
    return data_frame.shape[0]


def getColumnNames(data_frame: pd.DataFrame) -> list[str]:
    """Returns a list containing every column names of data_frame

    Args:
        data_frame (pd.DataFrame): a panda data frame

    Returns:
        list[str]: list of the column names of data_frame
    """
    return list(data_frame.columns)


def getRows(
    data_frame: pd.DataFrame, last_row: int, first_row: int = 0
) -> pd.DataFrame:
    """In data_frame, returns all the rows whose indexes are between first_row and last_row.
    If first_row > last_row or last_row = 0 then it returns an empty data frame.

    Args:
        data_frame (pd.DataFrame): a panda data frame
        last_row (int): index of the last row to be extracted.
        first_row (int, optional): index of the first row to be extracted. Defaults to 0.

    Returns:
        pd.DataFrame: a truncated version of data_frame
    """
    return data_frame[first_row:last_row]


def getColumns(data_frame: pd.DataFrame, names: list[str]) -> pd.DataFrame:
    """Returns a panda data frame containing the columns specified by names.
    If names is empty then it returns an empty data frame.
    If the string contained in names does not refer to actual columns of data_frame,
    this function print an error message and return a None.

    Args:
        data_frame (pd.DataFrame): a panda data frame
        names (list[str]): list containing names of some columns of data_frame or a single string of a column name

    Returns:
        pd.DataFrame: a panda data frame containing only some columns of data_frame
    """
    try:
        return data_frame[names]
    except KeyError:
        print(
            "Unvalid column names. The strings in names do not refer to actual columns of your data frame"
        )
        return None


def getRowsWithModality(
    data_frame: pd.DataFrame, column: str, modality: str
) -> pd.DataFrame:
    """Returns all the rows in data_frame whose modality in the specific column match the specified modality.
    If the string column does not refers to an actual column of data_frame,
    this function print an error message and return a None.
    If modality does not refer to any of the modalities in column then it returns an empty data frame.

    Args:
        data_frame (pd.DataFrame): a panda data frame
        column (str): name of one column of data_frame
        modality (str): name of one of the modalities contained in the column of data_frame

    Returns:
        pd.DataFrame: a panda data frame containing the rows of data_frame whose modality in data_frame column
            match modality
    """
    try:
        return data_frame[data_frame[column] == modality]
    except KeyError:
        print(
            "Unvalid column name. The string in column do not refer to an actual column of your data frame"
        )
        return None


def transformColumnToList(data_frame: pd.DataFrame, column: str) -> list:
    """Returns a python list of all the datas contained in one specified column of a panda data frame.
    If the string column does not refer to an actual column of data_frame,
    this function print an error message and return a None.

    Args:
        data_frame (pd.DataFrame): a panda data frame
        column (str): name of one column of data_frame

    Returns:
        list: _description_
    """
    try:
        return data_frame[column].to_list()
    except KeyError:
        print(
            "Unvalid column name. The string in column do not refer to an actual column of your data frame"
        )
        return None


with sqlite3.connect("data/penguins.sqlite") as co:
    # Create a panda data frame from a sql query on penguins.sqlite
    penguins_df = pd.read_sql_query("SELECT * FROM penguins", co)
    nb_row_peng = getNbRows(penguins_df)
    # print("Number of rows : ", nb_row_peng)

    # DATA VISUALIZATION
    print(penguins_df.head())  # overview of the data frame

    trunc_peng = getRows(penguins_df, last_row=222, first_row=89)
    # print(trunc_peng)

    col_names = getColumnNames(penguins_df)
    # print(col_names)

    # extraction of species + island columns
    col_peng = getColumns(penguins_df, names=col_names[:2])
    # print(col_peng)

    # Extracting all rows refering to the Adelie specie
    adelies = getRowsWithModality(penguins_df, column="species", modality="Adelie")
    # print(adelies)

    # Extracting the body masses of females
    female_body_mass = getColumns(
        getRowsWithModality(penguins_df, column="sex", modality="female"),
        names="body_mass_g",
    )
    # print(female_body_mass)

    # Converting a column of the data frame in a python list
    bill_length_l = transformColumnToList(penguins_df, "bill_length_mm")
    # print(bill_length_l)

    # FREQUENCE TABLE
    freq_table_l = freq_table.createAllFreqTables(penguins_df)
    # print(freq_table_l[0])  # frequence table of the species
    # print(freq_table_l[1])  # frequence table of the islands
    # print(freq_table_l[6])  # frequence table of the sexes

    # HISTOGRAMS
    histogram.createHist(bill_length_l, col_names[2])
