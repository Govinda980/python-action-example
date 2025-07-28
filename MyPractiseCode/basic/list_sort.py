def list_sort_into_one_list():
    test_list = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
    sorted_list = [y for x in test_list for y in x]
    sorted_list.sort()
    print(sorted_list)


def sort_fun(x):
    return x[0]


def list_sort_based_each_list():
    test_list = [[1, 3, 2, 4, 5, 3], [2, 1, 2], [3, 2, 1]]
    [item.sort() for item in test_list]
    print(test_list)


def sort_based_on_first_element():
    test_list = [[1, 3, 2, 4, 5, 3], [4, 1, 2], [3, 2, 1]]
    sorted_list = sorted(test_list, key=lambda x: x[0])
    print(sorted_list)


"""
The original list is : [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
The sort order list is : ['d', 'c', 'a', 'b']
The sorted list is : [('d', 4), ('c', 3), ('a', 1), ('b', 2)]
"""


def sort_list_based_on_given_order():
    test_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
    order_list = ['d', 'c', 'a', 'b']
    test_list_order = [item for o in order_list for item in test_list if o == item[0]]
    print(test_list_order)


def is_list_sorted():
    test_list = [1, 4, 6, 5, 8, 10]
    flag = True
    for i in range(len(test_list) - 1):
        if test_list[i] > test_list[i + 1]:
            flag = False
            break
    if not flag:
        print("Not sorted...")
    else:
        print("Sorted...")


def sort_by_len_item():
    list_test = ["rohan", "amy", "sapna", "muhammad", "aakash", "raunak", "chinmoy"]
    # list_test.sort(key=len)
    # list_test.sort(reverse= True, key=len)
    sortedList = sorted(list_test, key=lambda x: len(x))
    print(sortedList)


def myfunc(n):
    return abs(n - 50)


def test_based_on_close():
    thislist = [100, 50, 65, 82, 23]
    thislist.sort(key=myfunc)
    print(thislist)


if __name__ == '__main__':
    # list_sort_into_one_list()
    # list_sort_based_each_list()
    # sort_based_on_first_element()
    # sort_list_based_on_given_order()
    # is_list_sorted()
    sort_by_len_item()
