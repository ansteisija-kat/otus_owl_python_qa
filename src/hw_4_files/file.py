import json
from pathlib import Path

CSV_FILE_PATH = Path("/Users/niacris/Downloads/books.csv")
JSON_FILE_PATH = Path("/Users/niacris/Downloads/users.json")

#f = open("result.json", "a")

with open(CSV_FILE_PATH, 'r') as b:
    books = []
    for line in b:
            # books = b.readline()
            # print('books: ')
            # print(books)
        line = line.split('\n')[0]
        books.append(line)
            #print(line)
    print('books: ')
    print(books)


with open(JSON_FILE_PATH, 'r') as u:
    ur = u.read()
    users = json.loads(ur)
    print('users: ')
    print(users)

my_json_string = json.dumps({'name': users[0]["name"], 'gender': users[0]["gender"], 'address': users[0]["address"], 'age': users[0]["age"],
                             'books': books[1]})

print('my_json_string: ')
print(my_json_string)


