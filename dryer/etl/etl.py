import json

f = open('data.json')
data = json.load(f)

print("hello world", data["env"])
