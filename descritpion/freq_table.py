import pandas as pd


def createFreqTable(data_frame: pd.DataFrame, column: str) -> pd.DataFrame:
    """Returns the frequency table of the specified column of a data frame.
    The frequency table consists in an data frame giving the name (if the column is a qualitative variable)
    or the number (if the column is a quantitative variable) of each modality and the number of occurences
    of this name/number.

    Args:
        data_frame (pd.DataFrame): a panda data frame
        column (str): Name of a column of the data frame

    Returns:
        pd.DataFrame: the frequency table of the given column
    """
    return data_frame[column].value_counts()


def createAllFreqTables(data_frame: pd.DataFrame) -> list[pd.DataFrame]:
    """Returns all the possible frequency tables of a data frame using createFreqTable function.
    Does not take into account

    Args:
        data_frame (pd.DataFrame): a panda data frame

    Returns:
        list[pd.DataFrame]: list of every frequency table of data_frame
    """
    freq_table = []
    for column in data_frame.columns:
        freq_table.append(createFreqTable(data_frame, column))
    return freq_table


# The following lines are executed only if you run specifically freq_table.py and are used to test the code above
if __name__ == "__main__":
    # UNIT TEST
    df = pd.DataFrame({"eyes": ["Bleu", "Vert", "Marron", "Bleu", "Bleu", "Marron"]})
    print(df)
    print(createFreqTable(df, "eyes"))  # Function is working
