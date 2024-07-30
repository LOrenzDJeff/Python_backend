import json

def search():
    file_path = 'thermalmapdataall.json'

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    list_of_dicts = []
    for item in data:
        list_of_dicts.append([item['latitude'], item['longitude'], item['rsrp']])
    return list_of_dicts

        
print(search())
