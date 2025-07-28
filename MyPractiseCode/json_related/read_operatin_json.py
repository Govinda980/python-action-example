import json


def convert_json_to_data():
    json_data = ' { "name": "Riyansh", "age": 2, "city":"Shivnagar"}'
    print(type(json_data))
    data_dic = json.loads(json_data)
    print(type(data_dic), data_dic)


def convert_to_json():
    details = {
        "name": "Riyansh", "age": 2, "city": "Shivnagar"
    }
    with open('dump.json', 'w+') as file:
        file.write(json.dumps(details))


def read_json_file():
    with open('data.json', 'r') as file:
        data = json.load(file)  # for file load but for json_obj use loads
        print(data)
        print("data--->", data['address'])


def test_json_related_datatype():  # data to json
    print(json.dumps({"name": "John", "age": 30}))
    print(json.dumps(["apple", "bananas"]))
    print(json.dumps(("apple", "bananas")))
    print(json.dumps("hello"))
    print(json.dumps(42))
    print(json.dumps(31.76))
    print(json.dumps(True))
    print(json.dumps(False))
    print(json.dumps(None))


def dic_to_json_indent_use():
    import json

    x = {
        "name": "John",
        "age": 30,
        "married": True,
        "divorced": False,
        "children": ("Ann", "Billy"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
        ]
    }

    print(type(x))
    # use four indents to make it easier to read the result:
    print(json.dumps(x, indent=4))


if __name__ == '__main__':
    read_json_file()
    # convert_json_to_data()
    # convert_to_json()
    # test_json_related_datatype()
    # dic_to_json_indent_use()
