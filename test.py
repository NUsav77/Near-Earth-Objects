# This is for testing purposes only

import json


class Inspect:
    pass


class Query:
    pass


class Interactive:
    pass


f = open('cad.json', )
data = json.load(f)
print(data['fields'])
for row in data['data']:
    if row[0] == "2002 PB" and "2000-Jan-01" in row[3]:
        for columns in range(len('fields')):
            print(f"{data['fields'][columns]} {row[columns]}")
f.close()
