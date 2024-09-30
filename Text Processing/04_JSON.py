import json

with open('std1.json', 'r') as file:
    reader = json.load(file)
    print(reader)