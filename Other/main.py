import json

def search():
    file_path = 'thermalmapdataall.json'

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    list_of_dicts = []
    for item in data:
        if item['cellID'] == '139956839':
            list_of_dicts.append([float(item['latitude']), float(item['longitude']), int(item['rsrp'])])
    return list_of_dicts

        
print(search())
