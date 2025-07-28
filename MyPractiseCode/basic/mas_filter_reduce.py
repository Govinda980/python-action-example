import functools

li = [1, 2, 3, 4]
sq_list = list(map(lambda x: x % 2 == 0, li))
print(sq_list)

li = list(filter(lambda x: x % 2 == 0, li))
print(li)

lis = [1, 3, 4, 10, 4]
sum_lis = functools.reduce(lambda x, y: x + y, lis)
print(sum_lis)


original_dict = {'a': 1, 'b': 2}
another_dict = {'b': 3, 'c': 4}
original_dict.update(another_dict)
print(original_dict)
print("*************************************************")
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1 | dict2
print(merged_dict)

merged_dict1 = {**dict1, **dict2}
print(merged_dict1)