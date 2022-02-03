import json

with open('config/config1.json') as json_file:
    data = json.load(json_file)

print("hello world", data["env"])
