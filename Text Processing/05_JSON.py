import json
my_dict = {
    "Name" : "Raj",
    "Languages" : ["English", 'Hindi'],
    "Age" : 32,
}

with open('std2.json', 'w') as file:
    writer = json.dump( my_dict, file)