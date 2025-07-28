import random


class ItemInRangeException(Exception):
    pass


def check_correct_item(list_test):
    for item in list_test:
        try:
            if 50 < item < 70:
                raise ItemInRangeException(f"Number {item} is is between range of 50 and 70")
            else:
                print("Item", item)
        except ItemInRangeException as e:
            print("Exception is", e)
            continue


test_list = random.sample(range(1, 100), 20)
check_correct_item(test_list)
