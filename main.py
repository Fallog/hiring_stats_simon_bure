import sqlite3
import pandas as pd

with sqlite3.connect("data/penguins.sqlite") as co:
    # Create a panda data frame from a sql query on penguins.sqlite
    penguins_df = pd.read_sql_query("SELECT * FROM penguins", co)
    nb_row_peng = penguins_df.shape[0]

    # DATA VISUALIZATION
    print(penguins_df.head())  # overview of the data frame

    last_rows_peng = penguins_df[300:nb_row_peng]  # extracting some rows
    bill_length = penguins_df.bill_length_mm  # extracting a column

    # Extracting all rows refering to the Adelie Specie
    adelies = penguins_df[penguins_df.species == "Adelie"]

    # Extracting the body masses of females
    female_body_mass = penguins_df[penguins_df.sex == "female"].body_mass_g

    # Extracting flipper length superiour to 200 of every penguin catch in 2009
    flip_lgt_2009 = penguins_df[penguins_df.year == 2009][
        penguins_df.flipper_length_mm > 200
    ]

    # Converting a column of

    # UNCOMMENT THE FOLLOWING LINES TO SEE THE RESULT OF THE PREVIOUS MANIPULATIONS
    # print(last_rows_peng)
    # print(bill_length)
    # print(adelies)
    # print(female_body_mass)
    # print(flip_lgt_2009)

    # FREQUENCE TABLE
    print(penguins_df.species.value_counts())
    print(penguins_df.flipper_length_mm.value_counts())
