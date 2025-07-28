# serialization is process of converting python object into json data and update into json files. (dump)
# deserialization id process of converting back json data to python object.(load)

import json

# serialization
details_obj = {'name': 'Riyansh', 'Age': 1, 'address': 'Dharahari-9'}
with open('serial.json', 'w+') as file:
    json.dump(details_obj, file)

# deserialization
with open('serial.json', 'r+') as file:
    python_obj = json.load(file)
    print(python_obj)
