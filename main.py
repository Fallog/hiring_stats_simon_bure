import sqlite3
import pandas as pd
from descritpion import freq_table
from descritpion import histogram


def getColumnNames(data_frame: pd.DataFrame) -> list[str]:
    """Returns a list containing every column names of data_frame

    Args:
        data_frame (pd.DataFrame): a panda data frame

    Returns:
        list[str]: list of the column names of data_frame
    """
    return list(data_frame.columns)


def extractRows(
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


def extractColumns(data_frame: pd.DataFrame, names: list[str]) -> pd.DataFrame:
    """Returns a panda data frame containing the columns specified by names.
    If names is empty then it returns an empty data frame.
    If the string contained in names do not refer to actual columns of data_frame,
    this function print an error message and return a None.

    Args:
        data_frame (pd.DataFrame): a panda data frame
        names (list[str]): list containing names of some columns of data_frame

    Returns:
        pd.DataFrame: a panda data frame containing only some columns of data_frame
    """
    try:
        return data_frame[names]
    except KeyError:
        print(
            "Unvalid column name. The strings in names do not refer to actual column of your data frame"
        )
        return None


with sqlite3.connect("data/penguins.sqlite") as co:
    # Create a panda data frame from a sql query on penguins.sqlite
    penguins_df = pd.read_sql_query("SELECT * FROM penguins", co)
    nb_row_peng = penguins_df.shape[0]

    # DATA VISUALIZATION
    print(penguins_df.head())  # overview of the data frame

    trunc_peng = extractRows(penguins_df, 222, 89)
    # print(trunc_peng)

    col_names = getColumnNames(penguins_df)
    # print(col_names)

    # extraction of species + island columns
    col_peng = extractColumns(penguins_df, col_names[:2])
    # print(col_peng)

    # Extracting all rows refering to the Adelie Specie
    adelies = penguins_df[penguins_df.species == "Adelie"]

    # Extracting the body masses of females
    female_body_mass = penguins_df[penguins_df.sex == "female"].body_mass_g

    # Extracting flipper length superiour to 200 of every penguin catch in 2009
    flip_lgt_2009 = penguins_df[penguins_df.year == 2009][
        penguins_df.flipper_length_mm > 200
    ]

    # Converting a column of the data frame in a python list
    bill_length_l = penguins_df.bill_length_mm.to_list()
    bill_depth_l = penguins_df.bill_depth_mm.to_list()
    flipper_length_l = penguins_df.flipper_length_mm.to_list()
    body_mass_l = penguins_df.body_mass_g.to_list()

    # UNCOMMENT THE FOLLOWING LINES TO SEE THE RESULT OF THE PREVIOUS MANIPULATIONS
    # print(last_rows_peng)
    # print(bill_length)
    # print(adelies)
    # print(female_body_mass)
    # print(flip_lgt_2009)

    # FREQUENCE TABLE
    # freq_table_l = []
    # for column in penguins_df.columns:
    #    # Storing the frequence table of each column of the data frame in a list
    #    freq_table_l.append(freq_table.createFreqTable(penguins_df, column))
    # print(freq_table_l[0])  # frequence table of the species
    # print(freq_table_l[1])  # frequence table of the islands
    # print(freq_table_l[6])  # frequence table of the sexes

    # HISTOGRAMS
    # histogram.createHist(penguins_df.species.to_list(), peng_col[0])
    # histogram.createHist(bill_length_l, peng_col[2])
    # histogram.createHist(bill_depth_l, peng_col[3])
    # histogram.createHist(flipper_length_l, peng_col[4])
    # histogram.createHist(body_mass_l, peng_col[5])
