def count_character_in_sequence():
    in_str = "aaabccccddd"
    # out_str - "a3b1c4d3"
    dic1 = {}
    out_str = ''
    uniq_list = []
    for i in in_str:
        if i not in uniq_list:
            uniq_list.append(i)
    print(uniq_list)
    for item in uniq_list:
        # dic1[item] = in_str.count(item)
        out_str += str(item) + str(in_str.count(item))
    print(out_str)


def second_highest():
    list_lest = [1, 2, 3, 4, 5, 100, 99, 99, 100]
    max_num = 0
    max_num2 = 0
    for item in list_lest:
        if item > max_num:
            max_num = item

    for item in list_lest:
        if item > max_num2 and item != max_num:
            max_num2 = item
    print(max_num2)


def second_highest_method_2():
    list_lest = [1, 2, 3, 4, 5, 100, 99, 99, 100]
    max_num1 = 0
    max_num2 = 0
    for item in list_lest:
        if item > max_num1:
            max_num2 = max_num1
            max_num1 = item
        elif item > max_num2 and item != max_num1:
            max_num2 = item
    print(max_num2)


def sort_dic_by_key():
    dic_test = {'name': 'Govinda', 'age': 26, 'org': 'TCS'}
    key_sort = list(dic_test.keys())
    key_sort.sort()
    dic_sort = {key_s: dic_test.get(key_s) for key_s in key_sort}
    print("sorted_dic---->\n", dic_sort)
    # sort using sorted
    dic_by_sorted = dict(sorted(dic_sort.items(), key=lambda item: item[0]))
    print("sorted by key using sorted() --->\n", dic_by_sorted)


def sort_by_val():
    dic_test = {'name': 'govinda', 'age': 'twenty', 'org': 'tcs', 'branch': 'automation'}
    val_sort = list(dic_test.values())
    val_sort.sort()
    print(val_sort)
    dic_val_sort = {key: val for x in val_sort for key, val in dic_test.items() if x == val}
    print("sort by value", dic_val_sort)
    # sort using value
    sort_by_val_sorted = dict(sorted(dic_test.items(), key=lambda item: item[1]))
    print("sorted by value using sorted methods\n", sort_by_val_sorted)


def matrix_create_sum():
    matrix = [[i * j for i in range(3)] for j in range(4)]
    print(matrix)
    sum_matrix = []
    for i in range(len(matrix[0])):
        sum_val = 0
        for j in range(len(matrix)):
            sum_val += matrix[j][i]
        sum_matrix.append(sum_val)
    print(sum_matrix)


def transpose_matrix():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    output = [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    req_matrix = [[0 for row in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            req_matrix[i][j] = matrix[j][i]
    print(req_matrix)


if __name__ == '__main__':
    # count_character_in_sequence()
    # second_highest()
    # sort_dic_by_key()
    # sort_by_val()
    # second_highest_method_2()
    # matrix_create_sum()
    transpose_matrix()
