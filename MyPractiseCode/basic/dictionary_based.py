def sort_dic_by_key():
    myDict = {'Riyansh': 10, 'Omendra': 9,
              'Nitesh': 15, 'Anik': 2, 'Anis': 32}
    key_dic = (list(myDict.keys()))
    key_dic.sort()
    sorted_dic = {key: myDict.get(key) for key in key_dic}
    print(sorted_dic)


def sort_dic_based_on_value():

    myDict = {'Riyansh': 10, 'Omendra': 99,
              'Nitesh': 15, 'Anik': 2, 'Anis': 32}
    dic_val = list(myDict.values())
    dic_val.sort()
    sort_by_value = {key: value for value in dic_val for key, val1 in myDict.items() if value == val1}
    print(sort_by_value)


# sort_dic_by_key()
sort_dic_based_on_value()
