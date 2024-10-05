import os.path
import json
from pathlib import Path
import pandas as pd


CSV_FILE_PATH = Path(".../Downloads/books.csv")
JSON_FILE_PATH = Path(".../Downloads/users.json")


with open(CSV_FILE_PATH, 'r') as b:
    books = pd.read_csv(b, header=0).to_dict('records')
    all_books = []
    for book in books:
        all_books.append(
            {
                "title": book["Title"],
                "author": book["Author"],
                "pages": book["Pages"],
                "genre": book["Genre"]
            }
        )


with open(JSON_FILE_PATH, 'r') as u:
    ur = u.read()
    users = json.loads(ur)
    all_users = []
    for user in users:
        all_users.append(
            {
                "name": user["name"],
                "gender": user["gender"],
                "address": user["address"],
                "age": user["age"],
                "books": []
            }
        )

users_i = 0
for i in range(len(all_books)):
    all_users[users_i]["books"].append(all_books[i])
    users_i += 1

    if users_i == len(all_users):
        users_i = 0
        all_users[users_i]["books"].append(all_books[i])
        users_i += 1

with open('.../Downloads/result.json', 'w') as result:
    json_file = json.dumps(all_users)
    result.write(json_file)

