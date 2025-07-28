import json
with open('data.json') as f1:
    data = json.load(f1)
print(type(data))
print(data)

dic_data = {'name': 'John Doe', 'age': 29, 'email': 'johndoe@example.com', 'address': {'street': '123 Main St', 'city': 'Anytown', 'state': 'CA', 'postalCode': '12345'}, 'phoneNumbers': [{'type': 'home', 'number': '555-1234'}, {'type': 'work', 'number': '555-5678'}], 'children': [{'name': 'Jane Doe', 'age': 5}, {'name': 'Jake Doe', 'age': 3}], 'married': True, 'hobbies': ['reading', 'hiking', 'swimming']}
with open('test.json', 'w') as f1:
    json.dump(dic_data, f1)

