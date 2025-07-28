"""
Algorithm
First we find the smallest element and swap it with the first element.
    This way we get the smallest element at its correct position.
Then we find the smallest among remaining elements (or second smallest) and move it to its correct position by swapping.
We keep doing this until we get all elements moved to correct position.

"""


def selection_sort_alg():
    test_list = [1, 3, 5, 2, 22, 9]
    for i in range(len(test_list) - 1):
        min_idx = i
        for j in range(i + 1, len(test_list)):
            if test_list[j] < test_list[min_idx]:
                min_idx = j

        if min_idx != i:
            test_list[i], test_list[min_idx] = test_list[min_idx], test_list[i]
    print(test_list)


selection_sort_alg()
