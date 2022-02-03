"""
Provides some initial view
"""

import json

with open('config/config1.json', encoding='UTF-8') as json_file:
    data = json.load(json_file)

print("hello world", data["env"])
