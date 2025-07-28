def flatter(li):
    l1 = []
    for item in li:
        if isinstance(item, list):
            l1.extend(flatter(item))
        else:
            l1.append(item)
    return l1


li = [1, [2, [3, 4], 5], 6]
print(flatter(li))

test_list = [1, [2, [3, 4], 5], 6]

input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
