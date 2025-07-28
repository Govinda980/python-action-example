def binary_search(arr, key_ele):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if key_ele > arr[mid]:
            low = mid + 1
        elif key_ele < arr[mid]:
            high = mid - 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    test_list = [2, 3, 4, 10, 40]
    key = 10

    res = binary_search(test_list, key)
    print(res)
    if res != -1:
        print("found")
    else:
        print("not found")
