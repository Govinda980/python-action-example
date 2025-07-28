def sort_dic_by_val(name_age):
    sorted_dic = dict(sorted(name_age.items(), key=lambda d: d[1]))
    print(sorted_dic)


def sort_by_key(name_age):
    sorted_dic = dict(sorted(name_age.items(), key=lambda d: d[0]))
    print(sorted_dic)


def sort_by_key_wbf(name_age):
    key_val = list(name_age.keys())
    key_val.sort()
    dic_sort = {}
    for item in key_val:
        dic_sort[item] = name_age[item]
    print(dic_sort)


def sort_by_val_wbf(name_age):
    value = list(name_age.values())
    value.sort()
    print(value)
    sorted_dic = {key: item for item in value for key, val in name_age.items() if item == val}
    print(sorted_dic)


if __name__ == '__main__':
    name_age = {"Anik": 12, "Riyansh": 1, "Manish": 4, "Anish": 9, "Nitesh": 10, "Omendra": 22}
    sort_dic_by_val(name_age)
    sort_by_key(name_age)
    sort_by_key_wbf(name_age)
    sort_by_val_wbf(name_age)
