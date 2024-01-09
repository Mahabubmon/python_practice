import json

s = '{"name":"Mahabub","age":28,"city":"Lalbagh"}'

e = json.loads(s)

f = json.dumps(s)

print(f)

print(e["name"])