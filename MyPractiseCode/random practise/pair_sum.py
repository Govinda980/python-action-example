def pair_of_sum():
    test_list = [1, 2, 3, 4, 5, 6, 4, 7, 8, 4, 3, 2]
    target = 5
    pair_target = []
    for i in range(len(test_list)):
        for j in range(i + 1, len(test_list)):
            if test_list[i] + test_list[j] == target:
                pair_target.append((test_list[i], test_list[j]))

    print(pair_target)


# 9. Find a maximum and minimum value in a List without using any predefined function.


def find_max_min():
    test_list = [11, 2, 3, 4, 5, 6, 4, 70, 8, 4, 3, 2]
    max_val, min_val = 0, test_list[0]
    for item in test_list:
        if item > max_val:
            max_val = item
        if min_val > item:
            min_val = item

    print(max_val, min_val)


def find_second_largest():
    test_list = [11, 2, 3, 4, 5, 6, 4, 70, 8, 4, 3, 20]
    max_1_val, max_2_val = 0, 0
    for item in test_list:
        if item > max_1_val:
            max_2_val = max_1_val
            max_1_val = item
        elif item > max_2_val and max_1_val != max_2_val:
            max_2_val = item

    print("max_2", max_2_val)


if __name__ == '__main__':
    find_second_largest()
    pair_of_sum()
    find_max_min()
