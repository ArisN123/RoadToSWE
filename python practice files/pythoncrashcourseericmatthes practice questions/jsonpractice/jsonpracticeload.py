import json


file_path = 'fav_number.json'


with open(file_path, 'r') as opened_file:
    fav_number = json.load(opened_file)

print(f'your fav number is {fav_number}')