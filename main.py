import sqlite3

with sqlite3.connect("data/penguins.sqlite") as co:
    co.execute("SELECT * FROM penguins").fetchall()
