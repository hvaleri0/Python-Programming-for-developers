import json
from pathlib import Path

# To create/write a Json file:

movies = [
    {"id": 1, "title": "terminator", "year": 1989},
    {"id": 1, "title": "Kindergarten Cop", "year": 1993}
]

data = json.dumps(movies)
print(data)
Path("movies.json").write_text(data)  # write data to a json file!

# To read a Json file:
data = Path("movies.json").read_text()  # loading the Json
movies = json.loads(data)  # Parsing the Json
print(movies[1]['title'])
