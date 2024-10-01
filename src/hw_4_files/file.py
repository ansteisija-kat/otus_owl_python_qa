import json
from pathlib import Path
import pandas as pd

CSV_FILE_PATH = Path("/Users/niacris/Downloads/books.csv")
JSON_FILE_PATH = Path("/Users/niacris/Downloads/users.json")

#f = open("result.json", "a")

with open(CSV_FILE_PATH, 'r') as b:
    books = pd.read_csv(b, header=0).to_dict('records') # !!!
    print('books: ')
    print(books)


with open(JSON_FILE_PATH, 'r') as u:
    ur = u.read()
    users = json.loads(ur)
    print('users: ')
    print(users)


# TODO осталось раскидать книги по юзерам, книги замаплены как надо

my_json_string = json.dumps({'name': users[0]["name"], 'gender': users[0]["gender"], 'address': users[0]["address"], 'age': users[0]["age"],
                             'books': {...})

print('my_json_string: ')
print(my_json_string)


