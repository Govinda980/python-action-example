import logging
logging.basicConfig(level=logging.DEBUG)


def find_second_max():
    arr = [12, 1, 3, 4, 2, 22, 11, 111]
    first_max = 0
    second_max = 0
    logging.debug("Iteration over list....")
    for item in arr:
        if item > first_max:
            second_max = first_max
            first_max = item
        if item > second_max and item != first_max:
            second_max = item
    logging.debug("Second number is {0}".format(second_max))


find_second_max()
