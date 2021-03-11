import sqlite3
import json
from pathlib import Path

# * To write data to a database:

movies = json.loads(Path("movies.json").read_text())

with sqlite3.connect("db.sqlite") as conn:
    # Command = Instruction we send to the database to insert row:
    # Question marks "?" place holder for values supplied in the for loop
    command = "INSERT INTO Movies VALUES(?,?,?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()  # changes will be written to db, only needed when writing data to db

# * To read data from a database
with sqlite3.connect("db.sqlite") as conn:
    # Command = Instruction we send to the database to read whole table:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)  # returns an iterable cursor

    # for row in cursor:
    #     print(row)

    movies = cursor.fetchall()
    print(movies)
